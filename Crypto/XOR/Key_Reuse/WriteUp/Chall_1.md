## Enoncé :   

**Cipher_1** = dVNWVV1DUFAAZFdTRBVPRlYAZVdDWENFRU1hUkNBWwVFUhZwVxVTQF1SUhNyU1ZPQwNSTnZEQAdOVQBEF2RBRhVXWUpEFmdFVQxWUkJZdgA=


**Plain** = You cannot use hashcat to recover online accounts (like Gmail, Instagram, Facebook, Twitter, etc.), because hashcat has no way to work on online accounts.
**Cipher_2** = dF1WVwhDUlEAYlFTRURPRFUAZABDWRNFRB9hU0JBXFNFUxVwVkBTQVpSVhByU1tPQFRSTnJEQFlOVVZEFmFBREdXXUJEF2ZFVQlWV0JZdlZWV1tDU1cAZgdTREFPRFEAZVdDXUZFRB9hUhNBWABFUhlwVxZTQVpSVhByU1JPQFZST3JEQAdOVFBEFjVBREdXWEFEEmJFUVdWUxFZd11WVwxDU1EAYlFTR0BPRAAAZFRDWU9FRBphVhVBXFNFUBlwVxZTQFxSUxRyU1JPQFJSTnNEQFBOVQFEEjNBQUNXW0REFmNFVVxWU0dZd1ZWVwhDUwIAZgNTQRRPQFQAZ1FDWEFFREBhU0JBWVdFUhVwVkFTRQxSVhByU1ZPQVFST3JERAROUVxEEjNBQUNXWUBEFmdFVVxWU0NZdlFWVl1DU1EAYlFTRU9PRFUAZVZDWU5FREphUkdBWVdFVhBwV0tTQV5SUxNyV1NPQABSTydERFFOVFJEFmFBREpXXUJEF2ZFVQlWV0JZdlNWVwhDUlYAZgNTQUdPRAIAZABDXUZFRB9hUhNBWABFUhlwVxZTQVpSVhByU1JPQFZST3JEQAdOVFBEFjVBREdXWEFEEjc=

## Write Up

On recherche la chaine de caractère du cipher_1, pour se faire on a un autre texte en clair et sa version chiffré par la même clef.

On va donc faire un xor de la chaîne claire avec cipher_2.
Ainsi on obtient la clef qui à servit à chiffré la première chaîne.

On utilise cette dernière pour faire le xor de cipher_1.

On trouve donc le flag : GCTF{Brute_force_wont_help}
Avec la clef : Advanced Password Recovery