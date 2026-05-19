class Solution:
    # Encoding based on the delimiter ';'
    def encode(self, strs: List[str]) -> str:
        return ";".join(strs) if len(strs) > 0 else ";;"

    def decode(self, s: str) -> List[str]:
        return s.split(";") if s != ";;" else []
