all: upload

zip: drink.py
	zip deploy.zip drink.py
	cd .venv/lib/python2.7/site-packages; zip -r ../../../../deploy.zip *

upload: zip
	aws lambda update-function-code --function-name Drink --zip-file fileb://deploy.zip

clean:
	rm deploy.zip
