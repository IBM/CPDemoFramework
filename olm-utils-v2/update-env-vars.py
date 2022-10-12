import sys
server = sys.argv[1]
api_token = sys.argv[2]
kubeadmin_user = sys.argv[3]
kubeadmin_password = sys.argv[4]
icr_key = sys.argv[5]
lines = []
with open("env.sh") as f:
    lines = f.readlines()   
    lines[1] = server + "\n"
    lines[4] = api_token + "\n"
    lines[9] = kubeadmin_user + "\n"
    lines[10] = kubeadmin_password + "\n"
    lines[14] = icr_key + "\n"
    
with open("env.sh","w") as f:    
    f.writelines(lines)
