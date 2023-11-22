import hashlib

def crack_sha1_hash(hash, use_salts = False):
  password_arr = []
  read_and_add_to_write("top-10000-passwords.txt", password_arr)

  if use_salts:
    top_salts_password = {}
    top_salts = []
    read_and_add_to_write("known-salts.txt", top_salts)
    for bsalt in top_salts:
      for bpassword in password_arr:
        prepended = hashlib.sha1(bsalt + bpassword).hexdigest()
        appended = hashlib.sha1(bpassword + bsalt).hexdigest()
        top_salts_password[prepended] = bpassword.decode("utf-8")
        top_salts_password[appended] = bpassword.decode("utf-8")

    if hash in top_salts_password:
      return top_salts_password[hash]
    
      
  
  password_dict = {}
  for p in password_arr:
    hash_line = hashlib.sha1(p).hexdigest()
    password_dict[hash_line] = p.decode("utf-8")
   
  if hash in password_dict:
    return password_dict[hash]
  return "PASSWORD NOT IN DATABASE"


def read_and_add_to_write(filename, arr):
 
  with open(filename, "rb") as f:
    line = f.readline().strip()
    while line:
      arr.append(line)
      line = f.readline().strip()

