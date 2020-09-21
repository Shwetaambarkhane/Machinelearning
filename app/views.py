from django.shortcuts import render
import pandas as pd
import json

df = pd.read_csv('final_v2.csv')

# Create your views here.
def index(request):
	cnt_hindi=df.loc[df.LANGUAGE=='HINDI','LANGUAGE'].count()
	cnt_mar=df.loc[df.LANGUAGE=='MARATHI','LANGUAGE'].count()
	cnt_pun=df.loc[df.LANGUAGE=='PUNJABI','LANGUAGE'].count()
	cnt_eng=df.loc[df.LANGUAGE=='ENGLISH','LANGUAGE'].count()
	language1=[cnt_hindi,cnt_mar,cnt_pun,cnt_eng]
	a = df['LANGUAGE'].unique().tolist()
	b = language1
	a = json.dumps(a)
	cnt_love=df.loc[df.GENRE=='Love','GENRE'].count()
	cnt_pop=df.loc[df.GENRE=='Pop','GENRE'].count()
	cnt_party=df.loc[df.GENRE=='Party','GENRE'].count()
	cnt_life=df.loc[df.GENRE=='life','GENRE'].count()
	cnt_other=df.loc[df.GENRE=='Other','GENRE'].count()
	cnt_devotional=df.loc[df.GENRE=='Devotional','GENRE'].count()
	genre1=[cnt_love,cnt_pop,cnt_party,cnt_life,cnt_other,cnt_devotional]
	c=genre1
	d=df['GENRE'].unique().tolist()
	d=json.dumps(d)
	f=df['YEAR'].tolist()
	# m,n,o,p,q=0,0,0,0,0
	# for i in df['DURATION']:
	# 	if(i>='2:00' and i<'3:00'):
	# 	   m=m+1
	# 	elif(i>='3:00' and i<'4:00'):
	# 	   n=n+1
	# 	elif(i>='4:00' and i<'5:00'):
	# 	   o=o+1
	# 	elif(i>='5:00' and i<'6:00'):
	# 	   p=p+1
	# 	elif(i>='6:00'):
	# 	   q=q+1 
	# cnt_year=[m,n,o,p,q]
	# year_range=['1940-1960','1961-1980','1981-2000','2001-2010','2011-2020']
	# g=cnt_year
	# h=year_range
	# h=json.dumps(h)
	
	dh=df[df['LANGUAGE']=='HINDI']
	cnt_lh=dh.loc[dh.GENRE=='Love','GENRE'].count()
	cnt_lih=dh.loc[dh.GENRE=='life','GENRE'].count()
	cnt_dh=dh.loc[dh.GENRE=='Devotional','GENRE'].count()
	cnt_ph=dh.loc[dh.GENRE=='Party','GENRE'].count()
	cnt_oh=dh.loc[dh.GENRE=='Other','GENRE'].count()
	cnt_poh=dh.loc[dh.GENRE=='Pop','GENRE'].count()


	dp=df[df['LANGUAGE']=='PUNJABI']
	cnt_lp=dp.loc[dp.GENRE=='Love','GENRE'].count()
	cnt_lip=dp.loc[dp.GENRE=='life','GENRE'].count()
	cnt_dp=dp.loc[dp.GENRE=='Devotional','GENRE'].count()
	cnt_pp=dp.loc[dp.GENRE=='Party','GENRE'].count()
	cnt_op=dp.loc[dp.GENRE=='Other','GENRE'].count()
	cnt_pop=dp.loc[dp.GENRE=='Pop','GENRE'].count()



	dm=df[df['LANGUAGE']=='MARATHI']
	
	cnt_lm=dm.loc[dm.GENRE=='Love','GENRE'].count()
	cnt_lim=dm.loc[dm.GENRE=='life','GENRE'].count()
	cnt_dm=dm.loc[dm.GENRE=='Devotional','GENRE'].count()
	cnt_pm=dm.loc[dm.GENRE=='Party','GENRE'].count()
	cnt_om=dm.loc[dm.GENRE=='Other','GENRE'].count()
	cnt_pom=dm.loc[dm.GENRE=='Pop','GENRE'].count()


	de=df[df['LANGUAGE']=='ENGLISH']
	cnt_le=de.loc[de.GENRE=='Love','GENRE'].count()
	cnt_lie=de.loc[de.GENRE=='life','GENRE'].count()
	cnt_de=de.loc[de.GENRE=='Devotional','GENRE'].count()
	cnt_pe=de.loc[de.GENRE=='Party','GENRE'].count()
	cnt_oe=de.loc[de.GENRE=='Other','GENRE'].count()
	cnt_poe=de.loc[de.GENRE=='Pop','GENRE'].count()

	love=[cnt_lh,cnt_lp,cnt_lm,cnt_le]
	life=[cnt_lih,cnt_lip,cnt_lim,cnt_lie]
	devo=[cnt_dh,cnt_dp,cnt_dm,cnt_de]
	party=[cnt_ph,cnt_pp,cnt_pm,cnt_pe]
	other=[cnt_oh,cnt_op,cnt_om,cnt_oe]
	pop=[cnt_poh,cnt_pop,cnt_pom,cnt_poe]
	i=love
	j=life
	k=devo
	l=party
	m=other
	n=pop
	return render(request, 'app/index.html', {'a':a, 'b':b,'c':c,'d':d,'f':f,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n})

def index1(request):
	cnt_lm=df.loc[df.SINGERS=='LATA MANGESHKAR','SINGERS'].count()
	cnt_as=df.loc[df.SINGERS=='ARIJIT SINGH','SINGERS'].count()
	cnt_kk=df.loc[df.SINGERS=='KISHOR KUMAR','SINGERS'].count()
	cnt_ab=df.loc[df.SINGERS=='ASHA BHOSALE','SINGERS'].count()
	cnt_un=df.loc[df.SINGERS=='UDIT NARAYAN','SINGERS'].count()
	cnt_mr=df.loc[df.SINGERS=='MOHAMMED RAFI','SINGERS'].count()
	singer=[cnt_lm,cnt_as,cnt_kk,cnt_ab,cnt_un,cnt_mr]
	a=singer
	singer_name=['LATA MANGESHKAR','ARIJIT SINGH','KISHOR KUMAR','ASHA BHOSALE','UDIT NARAYAN','MOHAMMED RAFI']
	b=singer_name
	b=json.dumps(b)
	cnt_ts=df.loc[df.SINGERS=='TAYLOR SWIFT','SINGERS'].count()
	cnt_ag=df.loc[df.SINGERS=='ARIANA GRANDE','SINGERS'].count()
	cnt_es=df.loc[df.SINGERS=='ED SHEERAN','SINGERS'].count()
	cnt_b=df.loc[df.SINGERS=='BEYONCE','SINGERS'].count()
	cnt_jb=df.loc[df.SINGERS=='JUSTIN BIEBER','SINGERS'].count()
	cnt_cc=df.loc[df.SINGERS=='CAMILA CABELLO','SINGERS'].count()
	singer1=[cnt_ts,cnt_ag,cnt_es,cnt_b,cnt_jb,cnt_cc]
	singer1_name=['TAYLOR SWIFT','ARIANA GRANDE','ED SHERAN',' BEYONCE','JUSTIN BIEBER','CAMILA CABELLO']
	c=singer1
	d=singer1_name
	d=json.dumps(d)
	cnt_hs=df.loc[df.SINGERS=='HARDY SANDHU','SINGERS'].count()
	cnt_bb=df.loc[df.SINGERS=='BADSHAH','SINGERS'].count()
	cnt_gr=df.loc[df.SINGERS=='GURU RANDHAWA','SINGERS'].count()
	cnt_dd=df.loc[df.SINGERS=='DILJIT DOSANJH','SINGERS'].count()
	cnt_nk=df.loc[df.SINGERS=='NEHA KAKKAR','SINGERS'].count()
	cnt_kk=df.loc[df.SINGERS=='KANIKA KAPOOR','SINGERS'].count()
	singer3=[cnt_hs,cnt_bb,cnt_gr,cnt_dd,cnt_nk,cnt_kk]
	singer3_name=['HARDY SANDHU','BADSHAH','GURU RANDHAWA','DILJIT DOSANJH','NEHA KAKKAR','KANIKA KAPOOR']
	g=singer3
	h=singer3_name
	h=json.dumps(h)
	cnt_ka=df.loc[df.SINGERS=='USHA MANGESHKAR','SINGERS'].count()
	cnt_aa=df.loc[df.SINGERS=='AJAY-ATUL','SINGERS'].count()
	cnt_sm=df.loc[df.SINGERS=='SHANKAR MAHADEVAN','SINGERS'].count()
	cnt_um=df.loc[df.SINGERS=='ANIL MOHILE','SINGERS'].count()
	cnt_sb=df.loc[df.SINGERS=='NILESH MOHARIR','SINGERS'].count()
	cnt_ap=df.loc[df.SINGERS=='VAISHALI SAMANT','SINGERS'].count()
	singer2=[cnt_ka,cnt_aa,cnt_sm,cnt_um,cnt_sb,cnt_ap]
	singer2_name=['USHA MANGESHKAR','AJAY-ATUL','SHANKAR MAHADEVAN','ANIL MOHILE','NILESH MOHARIR','VAISHALI SAMANT']
	e=singer2
	f=singer2_name
	f=json.dumps(f)
	dh=df[df['LANGUAGE']=='HINDI']
	cnt_lh=dh.loc[dh.GENRE=='Love','GENRE'].count()
	cnt_lih=dh.loc[dh.GENRE=='life','GENRE'].count()
	cnt_dh=dh.loc[dh.GENRE=='Devotional','GENRE'].count()
	cnt_ph=dh.loc[dh.GENRE=='Party','GENRE'].count()
	cnt_oh=dh.loc[dh.GENRE=='Other','GENRE'].count()
	cnt_poh=dh.loc[dh.GENRE=='Pop','GENRE'].count()
	x=[cnt_lh,cnt_lih,cnt_dh,cnt_ph,cnt_oh,cnt_poh]
	y=['LOVE','LIFE','DEVOTIONAL','PARTY','OTHER','POP']

	dp=df[df['LANGUAGE']=='PUNJABI']
	cnt_lp=dp.loc[dp.GENRE=='Love','GENRE'].count()
	cnt_lip=dp.loc[dp.GENRE=='life','GENRE'].count()
	cnt_dp=dp.loc[dp.GENRE=='Devotional','GENRE'].count()
	cnt_pp=dp.loc[dp.GENRE=='Party','GENRE'].count()
	cnt_op=dp.loc[dp.GENRE=='Other','GENRE'].count()
	cnt_pop=dp.loc[dp.GENRE=='Pop','GENRE'].count()
	x1=[cnt_lp,cnt_lip,cnt_dp,cnt_pp,cnt_op,cnt_pop]


	dm=df[df['LANGUAGE']=='MARATHI']
	
	cnt_lm=dm.loc[dm.GENRE=='Love','GENRE'].count()
	cnt_lim=dm.loc[dm.GENRE=='life','GENRE'].count()
	cnt_dm=dm.loc[dm.GENRE=='Devotional','GENRE'].count()
	cnt_pm=dm.loc[dm.GENRE=='Party','GENRE'].count()
	cnt_om=dm.loc[dm.GENRE=='Other','GENRE'].count()
	cnt_pom=dm.loc[dm.GENRE=='Pop','GENRE'].count()
	x2=[cnt_lm,cnt_lim,cnt_dm,cnt_pm,cnt_om,cnt_pom]


	de=df[df['LANGUAGE']=='ENGLISH']
	cnt_le=de.loc[de.GENRE=='Love','GENRE'].count()
	cnt_lie=de.loc[de.GENRE=='life','GENRE'].count()
	cnt_de=de.loc[de.GENRE=='Devotional','GENRE'].count()
	cnt_pe=de.loc[de.GENRE=='Party','GENRE'].count()
	cnt_oe=de.loc[de.GENRE=='Other','GENRE'].count()
	cnt_poe=de.loc[de.GENRE=='Pop','GENRE'].count()
	x3=[cnt_le,cnt_lie,cnt_de,cnt_pe,cnt_oe,cnt_poe]
	aa=dh['YEAR'].tolist()
	bb=dp['YEAR'].tolist()
	cc=dm['YEAR'].tolist()
	dd=de['YEAR'].tolist()
	return render(request, 'app/index1.html', {'a':a, 'b':b,'c':c,'d':d,'e':e,'f':f,'x':x,'y':y,'x1':x1,'x2':x2,'x3':x3,'g':g,'h':h,'aa':aa,'bb':bb,'cc':cc,'dd':dd})
def sample1(request):
	dh=df[df['LANGUAGE']=='HINDI']
	a=dh.sort_values('RATING',ascending=False)

	return render(request,'app/sample1.html',{'a':a})
