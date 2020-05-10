mkdir "fullsize"
for f in *.*
	do magick convert $f -set filename:name %t fullsize/%[filename:name].jpg
done

dimensions=(1080 720 480 360 240)
mkdir -p "${dimensions[@]}"

for folder in "${dimensions[@]}"
do
	echo "${folder}"
	
	for f in *.jpg
		do magick convert $f -set filename:name %t -resize ${folder} -quality 80 ${folder}/%[filename:name].jpg
	done
	
	for f in *.JPG
		do magick convert $f -set filename:name %t %[filename:name].jpg
	done
done
