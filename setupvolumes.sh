docker volume create -d local-persist -o mountpoint=/home/tanmai/Documents/fuzzy-address-matching/mounts/data --name=mongodata


docker volume create -d local-persist -o mountpoint=/home/tanmai/Documents/fuzzy-address-matching/mounts/esdata2 --name=esdata2

docker volume create -d local-persist -o mountpoint=/home/tanmai/Documents/fuzzy-address-matching/connector --name=esconnector2
