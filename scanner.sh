#finds vulnerable printers with shodan
#make sure to shodan initiated with API-key
#script is easy to break but yeah

mkdir tempSho && cd tempSho

echo "looking for vulnerable printers with shodan"

results=$(shodan count port:9100 pjl)
echo "$results possible targets found"

echo "Downloading data form shodan..."
echo "how many printers do you want to target?(less than 100 advised)"
read size

shodan download port:9100 pjl --limit $size


shodan parse --fields ip_str port:9100.json.gz > ../ip.txt
cd ..

echo "targetting $size printers, saved in ip.txt"

rm -rf tempSho/
