import base64

# --- MATRICES ---
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
FP = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
E = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
KEY_SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
S_BOXES = [
[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]

def permute(b, t, bits):
    r = 0
    for p in t: r = (r << 1) | ((b >> (bits - p)) & 1)
    return r
def left_rotate(v, s, sz): return ((v << s) & ((1 << sz) - 1)) | (v >> (sz - s))
def sbox_substitution(b):
    r = 0
    for i in range(8):
        c = (b >> (42 - 6*i)) & 0x3F
        r = (r << 4) | S_BOXES[i][((c & 0x20) >> 4) | (c & 1)][(c >> 1) & 0xF]
    return r
def generate_keys(k):
    keys = []
    k = permute(k, PC1, 64)
    l, r = (k >> 28) & 0xFFFFFFF, k & 0xFFFFFFF
    for s in KEY_SHIFT:
        l, r = left_rotate(l, s, 28), left_rotate(r, s, 28)
        keys.append(permute((l << 28) | r, PC2, 56))
    return keys
def des_block(b, keys):
    b = permute(b, IP, 64)
    l, r = (b >> 32) & 0xFFFFFFFF, b & 0xFFFFFFFF
    for k in keys:
        t = r
        r = permute(r, E, 32) ^ k
        r = permute(sbox_substitution(r), P, 32) ^ l
        l = t
    return permute((r << 32) | l, FP, 64)
def des_decrypt(data, key):
    keys = generate_keys(key)[::-1]
    res = b""
    for i in range(0, len(data), 8):
        res += des_block(int.from_bytes(data[i:i+8], "big"), keys).to_bytes(8, "big")
    return res

# --- LOGICA PLAYFAIR ---
def playfair_decrypt(ciphertext, keyword):
    keyword = keyword.upper().replace('J', 'I')
    matrix_str = ""
    for char in keyword + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix_str:
            matrix_str += char
            
    matrix = [list(matrix_str[i:i+5]) for i in range(0, 25, 5)]
    
    def get_pos(c):
        for r in range(5):
            for col in range(5):
                if matrix[r][col] == c: return r, col
        return -1, -1

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        c1, c2 = ciphertext[i], ciphertext[i+1]
        r1, col1 = get_pos(c1)
        r2, col2 = get_pos(c2)
        
        if r1 == r2:
            plaintext += matrix[r1][(col1 - 1) % 5] + matrix[r2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(r1 - 1) % 5][col1] + matrix[(r2 - 1) % 5][col2]
        else:
            plaintext += matrix[r1][col2] + matrix[r2][col1]
            
    return plaintext, matrix

# --- PROGRAMA PRINCIPAL ---
def main():
    target_b64 = "h+F7XMoHpF0="
    target_bytes = base64.b64decode(target_b64)
    
    playfair_ciphertext = "SHPETXSQZNSPLBMBWFFKCEBRBQMVQSEGOLRBLGXPPSUXHWLGXPDLSZSNAZINELFTEQRGTSRIFWKBRGZVNPWKBQPGPBMZOMGEQMXPHGUFDIKBSCMGQMSHVZXTQMFXFOGPSHBWIOSNOQNPWKKCOQMFAVSHSMFOSNDKHGMVSZSHQPIYSQAVPNEGCERZQBQOKSSCOFOHPYQSBKQOZSHPFKEGKCRLSNQOIKOQOWPSTDPSBRAVGMVZQZKGFRZVVPZVSHPGVAOHRBGEZVEQHGWMKSNSZSRZPHZVPSZSIRDLSNAZINDLOBFWSKGPZSMZQZOWMCAVSHGRMPXGNSPGFPKFHBMGSQSGPEKGQSFSSNOWBLPYSQKBSQBRQSEFSGKSKSUXHWLGXPZSZSNSZKRGFZQPOQDYSXTFRZQMPQRGXECNZPCEGLBQNQPCMESNOWBLPYSCGSOHQPFSRIFWKBQBDTQOQNDOZVMIZPUFDIKBSCNGRYCYBLQGBQOQZAMRZPBRPESNGRQEPESNVPVZBKZVVPPSKSSPQBKGBKQOBKWHKDZVYMMGMQZLKEIOEQGLBRWHUXFOSPZSGPGFQOGKAV"

    print("Iniciando ataque de diccionario sobre DES...")
    playfair_key = None
    
    try:
        with open("words.txt", "r") as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        print("Error: El archivo 'words.txt' no se encuentra.")
        return

    for word in words:
        if len(word) != 8: continue
        
        key_int = int.from_bytes(word.encode("utf-8"), "big")
        decrypted_bytes = des_decrypt(target_bytes, key_int)
        
        try:
            # Si se puede decodificar a texto, es muy probable que sea la llave
            text = decrypted_bytes.decode("ascii")
            if text.isalpha():
                print(f"[EXITO] Llave DES encontrada: '{word}'")
                print(f"[EXITO] Clave para Playfair obtenida: '{text}'")
                playfair_key = text
                break
        except UnicodeDecodeError:
            pass # Era basura binaria, seguimos probando

    if playfair_key:
        print("\nGenerando matriz Playfair y descifrando el mensaje final...")
        pf_plaintext, matrix = playfair_decrypt(playfair_ciphertext, playfair_key)
        
        print("\nMatriz Playfair resultante:")
        for row in matrix:
            print(" ".join(row))
            
        print("\n--- Mensaje Oculto Descifrado ---")
        print(pf_plaintext)
    else:
        print("No se encontro la clave en el diccionario.")

if __name__ == "__main__":
    main()