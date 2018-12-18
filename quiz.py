from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb9UtrinVVseALPzk9Imb8ber3vG8rvnO73TEtwIhVb0Op1aW5GlZB_DIAswciyWijnC-2tsgndTaWqMOOBEAqcS0O9O6egYaZjsXvZ56BH7PA-a7KDMFovgcmX9IJtvzO1HpvYURFAln0v3walMubqit7BP4X9ya9P9D44OXFOZeVQUReuGdFMxJWp6aAGLhDgtw0'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()