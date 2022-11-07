from services.generate import Generate

try:
    path = Generate.generate_keypair()
    path = path.split('_privkey.')
    print(f'Keypair generated at {path[0]}_privkey.pem and {path[0]}_pubkey.pub')
except:
    print('Failed to generate keypair')
