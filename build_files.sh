echo " BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 maange.py collectstatic --noinput --clear
echo " BUILD END"