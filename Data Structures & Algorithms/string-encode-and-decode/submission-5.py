class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "empty"
        encode ="_devdj1691_".join(strs)
        return encode

    def decode(self, s: str) -> List[str]:
        if s=="empty":
            return []
        decode=s.split("_devdj1691_")
        return decode
