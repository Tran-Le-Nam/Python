import os, re, codecs #thư viện hệ thống, thay thế theo biểu thức chính qui, bảng mã utf8
ThuMucLamViec=os.getcwd()
ThuMucFileTeXGoc=ThuMucLamViec + '\\Filegoc'
os.chdir(ThuMucFileTeXGoc)
ThuMucLuuFile=ThuMucLamViec + '\\FileTam'
if not(os.path.exists(ThuMucLuuFile)):
	os.mkdir(ThuMucLuuFile)

Cacfile=os.listdir(ThuMucFileTeXGoc) #Danh sách các file được chứa trong thư mục ThuMucFileTeXGoc
Tempt=''
Lop={
	'0':'Lop10',
	'1':'Lop11',
	'2':'Lop12',
	'6':'Lop6',
	'7':'Lop7',
	'8':'Lop8',
	'9':'Lop9'
}
Mon={
	'D':'DS',
	'H':'HH',
	'X':'XS',
	'T':'TCST',
	'K':'KNTC',
	'C':'CD'

}
Chuong={
	'1':'Chuong1',
	'2':'Chuong2',
	'3':'Chuong3',
	'4':'Chuong4',
	'5':'Chuong5',
	'6':'Chuong6',
	'7':'Chuong7',
	'8':'Chuong8',
	'9':'Chuong9',
}
Bai={
	'1':'Bai1',
	'2':'Bai2',
	'3':'Bai3',
	'4':'Bai4',
	'5':'Bai5',
	'6':'Bai6',
	'7':'Bai7',
	'8':'Bai8',
	'9':'Bai9'	
}
Muc={
	'Y':'Muc1',
	'B':'Muc2',
	'K':'Muc3',
	'G':'Muc4',
	'T':'Muc5'
}

A=[] #Mãng lưu các câu hỏi
#Khởi tạo mãng tên
DitID={} #Lưu ID thành số thứ tự của mãng A
DitSO={} #dịch ngược số thứ tự của mãng A thành ID
i=0
for l,tl in Lop.items():
	for s,ts in Mon.items():
		for c,tc in Chuong.items():
			for m,tm in Muc.items():
				for b,tb in Bai.items():
					for dang in range(1,12):
						i+=1
						Ten='['+l+s+c+m+b+'-'+str(dang)+']'
						DitID[Ten]=i
						DitSO[i]=Ten
						A.append([])

B=[] #lưu tên và số các ID có câu hỏi
for File in Cacfile:
	if File.endswith('.tex'):
		Noidung=codecs.open(File, 'r', 'utf-8-sig').read()
		Noidung=re.sub('\\\\begin{(\\w\\w)}','\n\\\\begin{\\1}',Noidung)
		Noidung=re.sub('\\\\end{(\\w\\w)}','\n\\\\end{\\1}',Noidung)
		CH=re.findall('\\\\begin{\\w\\w}(.*?)\\\\end{\\w\\w}',Noidung,re.DOTALL) 
		for cau in CH:
			ID=re.findall('\\[[\\d][DHKCTX][\\d+][YBKGT][\\d]-[\\d+]\\]',cau)
			for file in ID:
				A[DitID[file]].append(cau)
				Kiemtra=True
				for i in range(len(B)):
					if B[i]==DitID[file]:
						Kiemtra=False
				if Kiemtra:
					B.append(DitID[file])

#Ghi kết quả lọc ra file
for so in B:
	Tempt=''
	for cau in A[so]:
		Tempt+='\n%%%================================%%%\n'\
			+'\\begin{ex}' + cau + '\n\\end{ex}'
	Tempt=Tempt.strip()
	Tfile=ThuMucLuuFile + '\\' + DitSO[so] + '.tex'
	with codecs.open(Tfile,'w','utf-8') as (f):
		f.write(Tempt)
		f.close()	

os.startfile(ThuMucLuuFile)
