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