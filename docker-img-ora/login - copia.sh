echo "validando instancia, usuario y contraseña"

if [ -z ${user+x} ]; then echo ERROR:User is unset. See readme file.; else echo User is set; fi;
if [ -z ${password+x} ]; then echo ERROR: Password is unset. See readme file.; else echo Password is set.; fi;
if [ -z ${instance+x} ]; then echo ERROR: Instance is unset. See readme file. ; else echo Instance is set; fi;

if [ -z ${user+x} ] || [ -z ${password+x} ] || [ -z ${instance+x} ]; then 
echo ""
else 
sqlplus $user/$password@$instance @/sql/caller.sql;
fi;