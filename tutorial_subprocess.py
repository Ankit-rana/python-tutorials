# subprocess is used to run external command 
# lets try generating random number without library in python3.6
import subprocess

out = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(out.stderr)
print(out.returncode) # if you want to raise exception rather than giving error code, use check=True
bout = out.stdout # byte class object
sout = bout.decode() # we can put encoding/text=True in run to get out as string rather byte 
print(sout)   

# to make output of one run command into input of another run, pass input=out.stdout in run2



# Note: to get environment variable, use os.environ["VAR"]