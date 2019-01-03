from collections import namedtuple, Counter

Claim = namedtuple('Claim','id, from_left, from_top, width, height')

class CalculatedClaim(Claim):
    @staticmethod
    def from_string(s):
        id, _, offset, size = s.split()
        from_left, _, from_top = offset.partition(',')
        from_top = from_top[:-1]
        width, _, height = size.partition('x')
        return CalculatedClaim(id,
                               int(from_left),
                               int(from_top),
                               int(width),
                               int(height))
    def squares(self):
        squares = []
        for x in range(self.from_left, self.from_left + self.width):
            for y in range(self.from_top, self.from_top + self.height):
                squares.append( (x, y) )
        return squares

# Input
with open('input/3', 'r') as f:
    claim_str_list = f.read().split('\n')

claims_per_square = Counter()
for claim_str in claim_str_list:
    if claim_str:
        claim = CalculatedClaim.from_string(claim_str)
        claims_per_square.update(claim.squares())

print("Total number of contested squares: ")
print(sum(x > 1 for x in claims_per_square.values()))

for claim_str in claim_str_list:
    if claim_str:
        claim = CalculatedClaim.from_string(claim_str)
        claim_squares = claim.squares()
        good_squares = [sq for sq in claim_squares if claims_per_square[sq]==1]
        if len(good_squares)==len(claim_squares):
            print("Singular claim: " + claim.id)
            break
