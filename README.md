# photoshare

# Stupid simple photo sharing application. Share photos 
# backed by s3 bucket with friends and family

# Use case 1: I want to share photos in a large collection (album) with family members


# photos - have an owner
# albums - have an owner, multiple photos
# users
# groups - have permission to access albums


running postgres:

docker run --rm --name postgres-db -p 5432:5432 -e POSTGRES_PASSWORD=n0password1 -d postgres
$> docker run -d -p 5432:5432 --name postures_db -e POSTGRES_PASSWORD=n0password1 postgres 
$> docker ps # to get the ID used below:
$> docker exec -it <ID> psql -U postgres

psql -h localhost -p 5432 -U postgres -W

# bullshit related to clang needing ssl version: "ld: library not found for -lssl"
$pip3 install psycopg2
> error: ld: library not found for -lssl
$export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
$export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"
$pip3 install psycopg2
> works now