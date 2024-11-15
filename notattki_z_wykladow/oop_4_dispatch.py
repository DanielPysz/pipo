pdb = """HEADER    IMMUNOGLOBULIN BINDING PROTEIN          15-MAY-91   2GB1
ATOM    135  CA  ASN A   8       8.137  -5.541   0.030  1.00  0.11           C 
SEQRES   5 A   56  THR VAL THR GLU
"""

def parse_atom(line: str):
    print("wczytuję atom")

def parse_header(line: str):
    print("wczytuję header")

def parse_strand(line: str):
    print("wczytuję wstęgę")

def parse_helix(line: str):
    print("wczytuję helisę")

class PdbDispatch:

    def __init__(self):
        self.__dispatch = { "ATOM": parse_atom,
                 "HEADER": parse_header,
                 "STRAND": parse_strand,
                "HELIX": parse_helix
                 }

    def __getitem__(self, item):
        return self.__dispatch[item]

    def register_action(self, line_type: str, action):
        self.__dispatch[line_type] = action


if __name__ == "__main__":

    disp = PdbDispatch()

    def moja_nowa_operacja(line: str):
        print("zupełnie nowa funkcja")

    disp.register_action("SEQRES", moja_nowa_operacja)

    for line in pdb.split("\n"):
        if len(line) <= 3: continue
        line_type = line[0:6].strip()
        action = disp[line_type]
        action(line)



# if __name__ == "__main__":
#     for line in pdb.split("\n"):
#         if len(line) <= 3: continue
#         line_type = line[0:6].strip()
#         if line_type == "ATOM":
#             parse_atom(line)
#         elif line_type == "HEADER":
#             parse_header(line)
#         elif line_type == "HELIX":
#             parse_helix(line)
#         elif line_type == "SHEET":
#             parse_strand(line)
#         elif line_type == "ATOM":
#             parse_atom(line)
#         else:
#             print("Nieznany format")
