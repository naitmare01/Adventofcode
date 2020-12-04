class IntCode:
  def __init__(self, mem):
    mem.extend([0] * 65536)
    self.mem = mem
    self.ptr = 0
    self.rel = 0
    self.ops = {
      # opcode: [function, default param modes]
      # param modes are matched to self.fetchers below
      # they are also used to modify param mode 2 to
      # determine fetch for that mode (see get_fetch_fun)
      1: [self.op_add, [0,0,1]],
      2: [self.op_mul, [0,0,1]],
      3: [self.op_input, [1]],
      4: [self.op_output, [0]],
      5: [self.op_beq, [0,0]],
      6: [self.op_bne, [0,0]],
      7: [self.op_lt, [0,0,1]],
      8: [self.op_eq, [0,0,1]],
      9: [self.op_relb, [0]],
      99: [self.op_halt, []]
    }
    self.fetchers = [
      self.position_fetch,
      self.immediate_fetch,
      self.relative_fetch,
      self.relative_addr
    ]

  def position_fetch(self, addr):
    # fetch param value from address (position mode)
    try:
      return self.mem[addr]
    except IndexError as ex:
      print("Index out of range %s" % addr)
      exit()

  def immediate_fetch(self, val):
    # passthrough of immediate param values,
    # for code consistency (immediate mode)
    return int(val)

  def relative_fetch(self, addr):
    return self.mem[self.rel + addr]

  def relative_addr(self, addr):
    return self.rel + addr

  def get_fetch_fun(self, mode, modifier):
    # accomodate for relative address/relative value modes.
    # this is mapped to default param modes,
    # so param mode 2 (relative) possibly gets augmented with +1
    # which will call relative_addr (which returns rel+addr) instead of
    # relative_fetch (which returns mem[rel+addr])
    if mode == 2:
      mode += modifier
    return self.fetchers[mode]

  def inc(self, i=1):
    # increase pointer
    self.ptr += i

  def op_beq(self, params):
    comp, addr = params
    if comp:
      self.ptr = addr
    else:
      self.inc()
    return True

  def op_bne(self, params):
    comp, addr = params
    if not comp:
      self.ptr = addr
    else:
      self.inc()
    return True

  def op_lt(self, params):
    v1, v2, addr = params
    self.mem[addr] = int(v1 < v2)
    self.inc()
    return True

  def op_eq(self, params):
    v1, v2, addr = params
    self.mem[addr] = int(v1 == v2)
    self.inc()
    return True

  def op_add(self, params):
    v1, v2, res_addr = params
    self.mem[res_addr] = v1 + v2
    self.inc()
    return True

  def op_mul(self, params):
    v1, v2, res_addr = params
    self.mem[res_addr] = v1 * v2
    self.inc()
    return True

  def op_input(self, params):
    dest_addr = params.pop()
    i = input("IntCode input> ")
    self.mem[dest_addr] = i
    self.inc()
    return True

  def op_output(self, params):
    out = params.pop()
    print("  "+str(out))
    self.inc()
    return True

  def op_relb(self, params):
    relchange = params.pop()
    self.rel += relchange
    self.inc()
    return True

  def op_halt(self, dummy_params):
    return False

  def parse(self):
    running = True
    while running:
      instr = str(self.mem[self.ptr])
      instr_param_modes = []

      if len(instr) > 2:
        op = int(instr[-2:])
        instr_param_modes = [int(c) for c in instr[:-2]]
        instr_param_modes.reverse()
      else:
        op = int(instr)

      # fetch operation method and default param modes
      op_fun, def_param_modes = self.ops[op]
      param_modes = def_param_modes[:] # copy list

      for i in range(len(instr_param_modes)):
        # replace instructon parameter modes over default modes,
        # if applicable
        param_modes[i] = instr_param_modes[i]

      params = []
      for i in range(len(def_param_modes)):
        raw = self.mem[self.ptr + 1] # add 1 to account for current op
        pm = param_modes[i]
        pm_modifier = def_param_modes[i]
        # fetch param with desired method and populate param list
        fetch_param = self.get_fetch_fun(pm, pm_modifier)
        params.append(fetch_param(raw))
        self.inc()  # increase pointer for each param

      running = op_fun(params) # op_fun will increase or set pointer as desired

    print("--- IntCode halted gracefully ---")

with open("input", "r") as f:
  raw = f.readline()
  code = [int(v) for v in raw.split(",")]


ic = IntCode(code)
ic.parse()
