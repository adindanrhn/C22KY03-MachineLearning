from flask import Flask, request, jsonify

import cv2
import easyocr
import json
import urllib.request
import numpy as np

import base64

from skimage import io
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/<name>')
def detect_ktp_ocr(url):

  base64_decode = base64.b64decode(name).decode('utf-8')
  url = "http://35.255.7.64/5000/uploads?url=/uploads/" + base64_decode

  img = io.imread(url)

  reader = easyocr.Reader(['en'])

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gaussian = cv2.GaussianBlur(src=gray,ksize=(3, 3),sigmaX=0,sigmaY=0)
  clahe = cv2.createCLAHE(clipLimit=2.00, tileGridSize=(12, 12))
  image = clahe.apply(gaussian)
  _, final_image = cv2.threshold(image, thresh=165, maxval=255, type=cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
  border_image = cv2.copyMakeBorder(
          src=final_image,
          top=20,
          bottom=20,
          left=20,
          right=20,
          borderType=cv2.BORDER_CONSTANT,
          value=(255, 255, 255))

  Result = reader.readtext(border_image, detail=0, width_ths=10)

  NIK=[]
  Nama=[]
  Tempat=[]
  Jenis=[]
  Alamat=[]
  Kel=[]
  Kec=[]
  Agama=[]
  Status=[]
  Pekerjaan=[]
  Kewarga=[]

  for i in Result:
    if 'NIK' in i:
      if ':' in i:
        NIK.append(i)
    if 'Nama' in i:
      if ':' in i:
        Nama.append(i)
    if 'Tempat' in i:
      if ':' in i:
        Tempat.append(i)
    if 'Jenis' in i:
      if ':' in i:
        Jenis.append(i)
    if 'Alamat' in i:
      if ':' in i:
        Alamat.append(i)
    if 'Kel' in i:
      if ':' in i:
        Kel.append(i)
    if 'Kec' in i:
      if ':' in i:
        Kec.append(i)
    if 'Agama' in i:
      if ':' in i:
        Agama.append(i)
    if 'Status' in i:
      if ':' in i:
        Status.append(i)
    if 'Pekerjaan' in i:
      if ':' in i:
        Pekerjaan.append(i)
    if 'Kewarga' in i:
      if ':' in i:
        Kewarga.append(i)

  remove = ':'

  if NIK != []:
    NIK=NIK[0].split(remove)[1].lstrip()
    print(NIK)
  else:
    NIK='Fill in the blank'
    print(NIK)

  if Nama != []:
    Nama=Nama[0].split(remove)[1].lstrip()
    print(Nama)
  else:
    Nama='Fill in the blank'
    print(Nama)

  if Tempat != []:
    Tempat=Tempat[0].split(remove)[1].lstrip()
    print(Tempat)
  else:
    Tempat='Fill in the blank'
    print(Tempat)

  if Jenis != []:
    Jenis=Jenis[0].split(remove)[1].lstrip().split(' ')[0]
    print(Jenis)
  else:
    Jenis='Fill in the blank'
    print(Jenis)

  if Alamat != []:
    Alamat=Alamat[0].split(remove)[1].lstrip()
    print(Alamat)
  else:
    Alamat='Fill in the blank'
    print(Alamat)

  if Kel != []:
    Kel=Kel[0].split(remove)[1].lstrip()
    print(Kel)
  else:
    Kel='Fill in the blank'
    print(Kel)

  if Kec != []:
    Kec=Kec[0].split(remove)[1].lstrip()
    print(Kec)
  else:
    Kec='Fill in the blank'
    print(Kec)

  if Agama != []:
    Agama=Agama[0].split(remove)[1].lstrip()
    print(Agama)
  else:
    Agama='Fill in the blank'
    print(Agama)

  if Status != []:
    Status=Status[0].split(remove)[1].lstrip()
    print(Status)
  else:
    Status='Fill in the blank'
    print(Status)

  if Pekerjaan != []:
    Pekerjaan=Pekerjaan[0].split(remove)[1].lstrip()
    print(Pekerjaan)
  else:
    Pekerjaan='Fill in the blank'
    print(Pekerjaan)

  if Kewarga != []:
    Kewarga=Kewarga[0].split(remove)[1].lstrip()
    print(Kewarga)
  else:
    Kewarga='Fill in the blank'
    print(Kewarga)

  ktp_dict={
      'nik' : NIK,
      'nama' : Nama,
      'ttl' : Tempat,
      'jenis' : Jenis,
      'alamat' : {
          'alamat' : Alamat,
          'kel' : Kel,
          'kec' : Kec
      },
      'agama' : Agama,
      'status' : Status,
      'pekerjaan' : Pekerjaan,
      'kwn' : Kewarga
  }

  return jsonify(ktp_dict)
