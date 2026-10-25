#!/usr/bin/env python3
"""Compila y firma el APK de Casa en Orden (se ejecuta solo en GitHub Actions)."""
FILES = {'AndroidManifest.xml': '<?xml version="1.0" encoding="utf-8" standalone="no"?>\n<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.casaenorden.app">\n    <application android:allowBackup="true" android:icon="@mipmap/ic_launcher" android:label="Casa en Orden">\n        <activity android:configChanges="keyboardHidden|orientation|screenSize" android:exported="true" android:name="com.casaenorden.app.MainActivity" android:theme="@android:style/Theme.Material.Light.NoActionBar" android:windowSoftInputMode="adjustResize">\n            <intent-filter>\n                <action android:name="android.intent.action.MAIN"/>\n                <category android:name="android.intent.category.LAUNCHER"/>\n            </intent-filter>\n        </activity>\n    </application>\n</manifest>\n', 'smali/com/casaenorden/app/MainActivity.smali': '.class public Lcom/casaenorden/app/MainActivity;\n.super Landroid/app/Activity;\n\n.field private web:Landroid/webkit/WebView;\n\n.method public constructor <init>()V\n    .locals 0\n    invoke-direct {p0}, Landroid/app/Activity;-><init>()V\n    return-void\n.end method\n\n.method protected onCreate(Landroid/os/Bundle;)V\n    .locals 3\n    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V\n    new-instance v0, Landroid/webkit/WebView;\n    invoke-direct {v0, p0}, Landroid/webkit/WebView;-><init>(Landroid/content/Context;)V\n    iput-object v0, p0, Lcom/casaenorden/app/MainActivity;->web:Landroid/webkit/WebView;\n    invoke-virtual {v0}, Landroid/webkit/WebView;->getSettings()Landroid/webkit/WebSettings;\n    move-result-object v1\n    const/4 v2, 0x1\n    invoke-virtual {v1, v2}, Landroid/webkit/WebSettings;->setJavaScriptEnabled(Z)V\n    invoke-virtual {v1, v2}, Landroid/webkit/WebSettings;->setDomStorageEnabled(Z)V\n    const-string v1, "AndroidVoz"\n    invoke-virtual {v0, p0, v1}, Landroid/webkit/WebView;->addJavascriptInterface(Ljava/lang/Object;Ljava/lang/String;)V\n    new-instance v1, Lcom/casaenorden/app/Cliente;\n    invoke-direct {v1}, Lcom/casaenorden/app/Cliente;-><init>()V\n    invoke-virtual {v0, v1}, Landroid/webkit/WebView;->setWebViewClient(Landroid/webkit/WebViewClient;)V\n    invoke-virtual {p0, v0}, Lcom/casaenorden/app/MainActivity;->setContentView(Landroid/view/View;)V\n    const-string v1, "file:///android_asset/index.html"\n    invoke-virtual {v0, v1}, Landroid/webkit/WebView;->loadUrl(Ljava/lang/String;)V\n    return-void\n.end method\n\n.method public dictar()V\n    .locals 2\n    .annotation runtime Landroid/webkit/JavascriptInterface;\n    .end annotation\n    new-instance v0, Lcom/casaenorden/app/VozTarea;\n    invoke-direct {v0, p0}, Lcom/casaenorden/app/VozTarea;-><init>(Lcom/casaenorden/app/MainActivity;)V\n    iget-object v1, p0, Lcom/casaenorden/app/MainActivity;->web:Landroid/webkit/WebView;\n    invoke-virtual {v1, v0}, Landroid/view/View;->post(Ljava/lang/Runnable;)Z\n    return-void\n.end method\n\n.method public startVoz()V\n    .locals 3\n    new-instance v0, Landroid/content/Intent;\n    const-string v1, "android.speech.action.RECOGNIZE_SPEECH"\n    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V\n    const-string v1, "android.speech.extra.LANGUAGE_MODEL"\n    const-string v2, "free_form"\n    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;\n    const-string v1, "android.speech.extra.LANGUAGE"\n    const-string v2, "es-AR"\n    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;\n    const-string v1, "android.speech.extra.PROMPT"\n    const-string v2, "Dec\\u00ed lo que quer\\u00e9s anotar"\n    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;\n    const/16 v1, 0x6d\n    :ts\n    invoke-virtual {p0, v0, v1}, Landroid/app/Activity;->startActivityForResult(Landroid/content/Intent;I)V\n    :te\n    return-void\n    .catch Landroid/content/ActivityNotFoundException; {:ts .. :te} :ca\n    :ca\n    move-exception v0\n    const-string v0, "window.onVozError()"\n    iget-object v1, p0, Lcom/casaenorden/app/MainActivity;->web:Landroid/webkit/WebView;\n    const/4 v2, 0x0\n    invoke-virtual {v1, v0, v2}, Landroid/webkit/WebView;->evaluateJavascript(Ljava/lang/String;Landroid/webkit/ValueCallback;)V\n    return-void\n.end method\n\n.method protected onActivityResult(IILandroid/content/Intent;)V\n    .locals 4\n    invoke-super {p0, p1, p2, p3}, Landroid/app/Activity;->onActivityResult(IILandroid/content/Intent;)V\n    const/16 v0, 0x6d\n    if-ne p1, v0, :fin\n    const/4 v0, -0x1\n    if-ne p2, v0, :fin\n    if-eqz p3, :fin\n    const-string v0, "android.speech.extra.RESULTS"\n    invoke-virtual {p3, v0}, Landroid/content/Intent;->getStringArrayListExtra(Ljava/lang/String;)Ljava/util/ArrayList;\n    move-result-object v0\n    if-eqz v0, :fin\n    invoke-virtual {v0}, Ljava/util/ArrayList;->isEmpty()Z\n    move-result v1\n    if-nez v1, :fin\n    const/4 v1, 0x0\n    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;\n    move-result-object v0\n    check-cast v0, Ljava/lang/String;\n    invoke-static {v0}, Lorg/json/JSONObject;->quote(Ljava/lang/String;)Ljava/lang/String;\n    move-result-object v0\n    new-instance v1, Ljava/lang/StringBuilder;\n    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V\n    const-string v2, "window.onVoz("\n    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n    const-string v2, ")"\n    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;\n    move-result-object v0\n    iget-object v1, p0, Lcom/casaenorden/app/MainActivity;->web:Landroid/webkit/WebView;\n    const/4 v2, 0x0\n    invoke-virtual {v1, v0, v2}, Landroid/webkit/WebView;->evaluateJavascript(Ljava/lang/String;Landroid/webkit/ValueCallback;)V\n    :fin\n    return-void\n.end method\n', 'smali/com/casaenorden/app/VozTarea.smali': '.class public Lcom/casaenorden/app/VozTarea;\n.super Ljava/lang/Object;\n.implements Ljava/lang/Runnable;\n\n.field private final act:Lcom/casaenorden/app/MainActivity;\n\n.method public constructor <init>(Lcom/casaenorden/app/MainActivity;)V\n    .locals 0\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n    iput-object p1, p0, Lcom/casaenorden/app/VozTarea;->act:Lcom/casaenorden/app/MainActivity;\n    return-void\n.end method\n\n.method public run()V\n    .locals 1\n    iget-object v0, p0, Lcom/casaenorden/app/VozTarea;->act:Lcom/casaenorden/app/MainActivity;\n    invoke-virtual {v0}, Lcom/casaenorden/app/MainActivity;->startVoz()V\n    return-void\n.end method\n', 'smali/com/casaenorden/app/Cliente.smali': '.class public Lcom/casaenorden/app/Cliente;\n.super Landroid/webkit/WebViewClient;\n\n.method public constructor <init>()V\n    .locals 0\n    invoke-direct {p0}, Landroid/webkit/WebViewClient;-><init>()V\n    return-void\n.end method\n\n.method public shouldOverrideUrlLoading(Landroid/webkit/WebView;Ljava/lang/String;)Z\n    .locals 3\n    const-string v0, "file:"\n    invoke-virtual {p2, v0}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z\n    move-result v0\n    if-eqz v0, :externo\n    const/4 v0, 0x0\n    return v0\n    :externo\n    new-instance v0, Landroid/content/Intent;\n    const-string v1, "android.intent.action.VIEW"\n    invoke-static {p2}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;\n    move-result-object v2\n    invoke-direct {v0, v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;Landroid/net/Uri;)V\n    const/high16 v1, 0x10000000\n    invoke-virtual {v0, v1}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;\n    invoke-virtual {p1}, Landroid/webkit/WebView;->getContext()Landroid/content/Context;\n    move-result-object v1\n    :ts\n    invoke-virtual {v1, v0}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V\n    :te\n    const/4 v0, 0x1\n    return v0\n    .catch Ljava/lang/Exception; {:ts .. :te} :ca\n    :ca\n    move-exception v1\n    const/4 v0, 0x1\n    return v0\n.end method\n'}
CODIGO_JS = "var AL='ABCDEFGHJKLMNPQRSTUVWXYZ23456789';\nfunction ror(x,n){return(x>>>n)|(x<<(32-n))}\nfunction sha256(msg){\n  var K=[],H=[],i,j,p=2,n=0;\n  for(;n<64;p++){var pr=1;for(j=2;j*j<=p;j++){if(p%j===0){pr=0;break}}if(pr){if(n<8)H[n]=Math.floor((Math.sqrt(p)%1)*4294967296);K[n]=Math.floor((Math.cbrt(p)%1)*4294967296);n++}}\n  var l=msg.length,w=new Array(64),bl=l*8,pd=new Uint8Array(((l+9+63)>>6)<<6);\n  pd.set(msg);pd[l]=128;var dv=new DataView(pd.buffer);dv.setUint32(pd.length-4,bl>>>0);dv.setUint32(pd.length-8,Math.floor(bl/4294967296));\n  var h=H.slice();\n  for(var off=0;off<pd.length;off+=64){\n    for(i=0;i<16;i++)w[i]=dv.getUint32(off+i*4);\n    for(i=16;i<64;i++){var s0=ror(w[i-15],7)^ror(w[i-15],18)^(w[i-15]>>>3),s1=ror(w[i-2],17)^ror(w[i-2],19)^(w[i-2]>>>10);w[i]=(w[i-16]+s0+w[i-7]+s1)|0}\n    var a=h[0]|0,b=h[1]|0,c=h[2]|0,d=h[3]|0,e=h[4]|0,f=h[5]|0,g=h[6]|0,hh=h[7]|0;\n    for(i=0;i<64;i++){var S1=ror(e,6)^ror(e,11)^ror(e,25),ch=(e&f)^(~e&g),t1=(hh+S1+ch+K[i]+w[i])|0,S0=ror(a,2)^ror(a,13)^ror(a,22),mj=(a&b)^(a&c)^(b&c),t2=(S0+mj)|0;hh=g;g=f;f=e;e=(d+t1)|0;d=c;c=b;b=a;a=(t1+t2)|0}\n    h[0]=(h[0]+a)|0;h[1]=(h[1]+b)|0;h[2]=(h[2]+c)|0;h[3]=(h[3]+d)|0;h[4]=(h[4]+e)|0;h[5]=(h[5]+f)|0;h[6]=(h[6]+g)|0;h[7]=(h[7]+hh)|0;\n  }\n  var o=new Uint8Array(32),ov=new DataView(o.buffer);for(i=0;i<8;i++)ov.setUint32(i*4,h[i]>>>0);return o}\nfunction hmac(k,m){var bs=64,kb=k.length>bs?sha256(k):k,ip=new Uint8Array(bs+m.length),op=new Uint8Array(bs+32);for(var i=0;i<bs;i++){var kv=kb[i]||0;ip[i]=kv^54;op[i]=kv^92}ip.set(m,bs);op.set(sha256(ip),bs);return sha256(op)}\nfunction b32(b,n){var bits=0,val=0,out='';for(var i=0;i<b.length&&out.length<n;i++){val=(val<<8)|b[i];bits+=8;while(bits>=5&&out.length<n){out+=AL[(val>>>(bits-5))&31];bits-=5}val&=(1<<bits)-1}return out}\nfunction normId(s){return String(s||'').toUpperCase().replace(/[^A-Z0-9]/g,'')}\nfunction codigoPara(id){var te=new TextEncoder();return b32(hmac(te.encode(CLAVE),te.encode('ceo1|'+normId(id))),16).replace(/(.{4})(?=.)/g,'$1-')}\n"

import os,sys,json,re,glob,shutil,subprocess,zipfile,hashlib,base64,datetime,urllib.request
ROOT=os.path.dirname(os.path.abspath(__file__))
W=os.path.join(ROOT,'_build'); OUT=os.path.join(ROOT,'out')
APKTOOL_URL='https://github.com/iBotPeaches/Apktool/releases/download/v2.10.0/apktool_2.10.0.jar'
YML="""version: 2.10.0
apkFileName: unsigned.apk
isFrameworkApk: false
usesFramework:
  ids:
  - 1
sdkInfo:
  minSdkVersion: '21'
  targetSdkVersion: '29'
packageInfo:
  forcedPackageId: '127'
versionInfo:
  versionCode: '%d'
  versionName: '%s'
resourcesAreCompressed: false
sharedLibrary: false
sparseResources: false
doNotCompress:
- resources.arsc
"""

def run(cmd,cwd=None):
    print('>',' '.join(cmd),flush=True); subprocess.run(cmd,cwd=cwd,check=True)

def escribir(ruta,txt):
    os.makedirs(os.path.dirname(ruta),exist_ok=True)
    with open(ruta,'w',encoding='utf-8',newline='\n') as f: f.write(txt)

def iconos(proj):
    from PIL import Image,ImageDraw
    def icono(size):
        S=size*4; im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
        d.rounded_rectangle([0,0,S-1,S-1],radius=int(S*0.22),fill='#35603F')
        o=S*0.14; w=S*0.72
        P=lambda x,y:(o+x*w,o+y*w)
        d.polygon([P(.5,.08),P(.96,.46),P(.04,.46)],fill='#FAF8F0')
        d.rectangle([*P(.14,.44),*P(.86,.92)],fill='#FAF8F0')
        d.rectangle([*P(.42,.62),*P(.58,.92)],fill='#35603F')
        d.line([P(.26,.66),P(.33,.74),P(.46,.56)],fill='#35603F',width=int(w*.05),joint='curve')
        return im.resize((size,size),Image.LANCZOS)
    for d_,s_ in [('mdpi',48),('hdpi',72),('xhdpi',96),('xxhdpi',144),('xxxhdpi',192)]:
        p=os.path.join(proj,'res','mipmap-'+d_); os.makedirs(p,exist_ok=True)
        icono(s_).save(os.path.join(p,'ic_launcher.png'))

def fuentes_css():
    d=os.path.join(W,'fonts'); os.makedirs(d,exist_ok=True)
    run(['npm','pack','@fontsource-variable/fraunces','@fontsource-variable/dm-sans'],cwd=d)
    for t in glob.glob(d+'/*.tgz'):
        sub=t[:-4]; os.makedirs(sub,exist_ok=True); run(['tar','xzf',t,'-C',sub])
    def f(n):
        r=glob.glob(d+'/**/'+n,recursive=True); assert r,n
        return base64.b64encode(open(r[0],'rb').read()).decode()
    return ("@font-face{font-family:'Fraunces';font-style:normal;font-weight:100 900;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}\n"
            "@font-face{font-family:'Fraunces';font-style:italic;font-weight:100 900;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}\n"
            "@font-face{font-family:'DM Sans';font-style:normal;font-weight:100 1000;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}\n"
            )%(f('fraunces-latin-wght-normal.woff2'),f('fraunces-latin-wght-italic.woff2'),f('dm-sans-latin-wght-normal.woff2'))

def parchear(s,cfg,clave):
    a="function dictar(dest){"; assert s.count(a)==1
    s=s.replace(a,a+"\n  if(window.AndroidVoz){window.vozDest=dest;setVm('Escuchando… hablá ahora.');window.AndroidVoz.dictar();return}",1)
    b="function addTask(txt){"; assert s.count(b)==1
    s=s.replace(b,"window.onVoz=function(t){if(window.vozDest==='tasks')addTask(t);else addShop(t,true);VMSG='Agregué: '+t;save();render()};\nwindow.onVozError=function(){setVm('No pude abrir el dictado. Usá el micrófono del teclado del celular.')};\n"+b,1)
    assert s.count('var GRATIS=true;')==1
    s=s.replace('var GRATIS=true;','var GRATIS=false;')
    q=lambda v:str(v).replace('\\','\\\\').replace("'","\\'")
    nuevo=r"""var CLAVE='%s',PRECIO='%s',PAGO_URL='%s',WA='%s';
%s
function miId(){var k='ceo_id';try{var v=localStorage.getItem(k);if(v)return v}catch(e){}var a=new Uint8Array(10),i,s='';try{crypto.getRandomValues(a)}catch(e){for(i=0;i<10;i++)a[i]=Math.floor(Math.random()*256)}for(i=0;i<10;i++)s+=AL[a[i]&31];s=s.slice(0,5)+'-'+s.slice(5);try{localStorage.setItem(k,s)}catch(e){}return s}
function paywall(){
  var d=document.getElementById('dlg'),id=miId();
  var h=`<h2>Desbloqueá el curso completo</h2><p class='sub'>Los módulos 2 al 5 se activan con un código personal, solo para este celular.</p>`;
  h+=PAGO_URL?`<p><b>1. Pagá</b> ${esc(PRECIO)}</p><button class='btn' id='pg' style='width:100%%;margin-bottom:12px'>Pagar con Mercado Pago</button>`:`<p><b>1. Pagá</b> el curso a quien te lo vendió.</p>`;
  h+=`<p><b>2. Mandá tu ID:</b> <span style='font-weight:800;letter-spacing:.05em'>${esc(id)}</span></p>`;
  if(WA)h+=`<button class='btn out' id='wa' style='width:100%%;margin-bottom:12px'>Enviar mi ID por WhatsApp</button>`;
  h+=`<p><b>3. Pegá tu código:</b></p><input id='cod' placeholder='XXXX-XXXX-XXXX-XXXX' autocapitalize='characters' autocomplete='off'><p class='sub' id='cm' role='status'></p><button class='btn' id='act' style='width:100%%'>Activar</button><button class='ghost' id='no' style='width:100%%;text-align:center'>Ahora no</button>`;
  d.innerHTML=h;d.showModal();
  var f;
  if(f=document.getElementById('pg'))f.onclick=function(){location.href=PAGO_URL};
  if(f=document.getElementById('wa'))f.onclick=function(){location.href='https://wa.me/'+WA+'?text='+encodeURIComponent('Hola! Ya pagué Casa en Orden. Mi ID es '+id)};
  document.getElementById('no').onclick=function(){d.close()};
  document.getElementById('act').onclick=function(){var c=normId(document.getElementById('cod').value),m=document.getElementById('cm');
    if(c&&c===normId(codigoPara(id))){S.pro=true;S.code=c;save();d.close();render()}else{m.textContent='Ese código no es válido para este celular. Revisá que esté completo.'}};
}
function paywallViejo(){""" % (q(clave),q(cfg.get('precio','')),q(cfg.get('pago','')),q(cfg.get('wa','')),CODIGO_JS)
    assert s.count('function paywall(){')==1
    s=s.replace('function paywall(){',nuevo,1)
    fin="\nrender();\n</script>"; assert s.count(fin)==1
    s=s.replace(fin,"\nif(S.pro&&normId(S.code||'')!==normId(codigoPara(miId())))S.pro=false;"+fin,1)
    return s

def firmar(src,dst,pem):
    from cryptography import x509
    from cryptography.x509.oid import NameOID
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.serialization import Encoding,PrivateFormat,NoEncryption,load_pem_private_key
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.serialization import pkcs7
    zin=zipfile.ZipFile(src)
    ents=[(i.filename,zin.read(i.filename)) for i in zin.infolist() if not i.is_dir() and not i.filename.startswith('META-INF/')]
    ents.sort(key=lambda e:(e[0]!='AndroidManifest.xml',e[0]))
    sha=lambda d:hashlib.sha256(d).digest(); b64=lambda d:base64.b64encode(d).decode()
    def wrap(t):
        b=t.encode(); o=[b[:70]]; b=b[70:]
        while b: o.append(b' '+b[:69]); b=b[69:]
        return b'\r\n'.join(o)+b'\r\n'
    main=b'Manifest-Version: 1.0\r\nCreated-By: 1.0 (Android)\r\n\r\n'
    secs=[wrap('Name: '+n)+wrap('SHA-256-Digest: '+b64(sha(d)))+b'\r\n' for n,d in ents]
    mf=main+b''.join(secs)
    sf=(b'Signature-Version: 1.0\r\nCreated-By: 1.0 (Android)\r\n'+wrap('SHA-256-Digest-Manifest: '+b64(sha(mf)))+wrap('SHA-256-Digest-Manifest-Main-Attributes: '+b64(sha(main)))+b'\r\n')
    for (n,d),s in zip(ents,secs): sf+=wrap('Name: '+n)+wrap('SHA-256-Digest: '+b64(sha(s)))+b'\r\n'
    if pem and pem.strip():
        key=load_pem_private_key(pem.encode(),None)
    else:
        print('AVISO: no hay KEYSTORE_PEM; se genera una clave nueva (la app no podrá actualizar a la anterior).')
        key=rsa.generate_private_key(public_exponent=65537,key_size=2048)
    name=x509.Name([x509.NameAttribute(NameOID.COMMON_NAME,'Casa en Orden')])
    now=datetime.datetime.now(datetime.timezone.utc)
    cert=(x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(key.public_key()).serial_number(x509.random_serial_number())
          .not_valid_before(now-datetime.timedelta(days=1)).not_valid_after(now+datetime.timedelta(days=365*30)).sign(key,hashes.SHA256()))
    sig=(pkcs7.PKCS7SignatureBuilder().set_data(sf).add_signer(cert,key,hashes.SHA256())
         .sign(Encoding.DER,[pkcs7.PKCS7Options.DetachedSignature,pkcs7.PKCS7Options.Binary,pkcs7.PKCS7Options.NoAttributes]))
    def zi(n):
        z=zipfile.ZipInfo(n,date_time=(2026,1,1,0,0,0)); z.external_attr=0o644<<16; return z
    with zipfile.ZipFile(dst,'w') as z:
        for n,d in [('META-INF/MANIFEST.MF',mf),('META-INF/CERT.SF',sf),('META-INF/CERT.RSA',sig)]:
            i=zi(n); i.compress_type=zipfile.ZIP_DEFLATED; z.writestr(i,d)
        for n,d in ents:
            i=zi(n); i.compress_type=zipfile.ZIP_STORED if n=='resources.arsc' else zipfile.ZIP_DEFLATED; z.writestr(i,d)

def main():
    cfg=json.load(open(os.path.join(ROOT,'config.json'),encoding='utf-8'))
    clave=os.environ.get('CLAVE_CODIGOS','').strip()
    if not clave: sys.exit('Falta el secreto CLAVE_CODIGOS')
    vc=10+int(os.environ.get('RUN_NUMBER','1')); vn='3.%s'%os.environ.get('RUN_NUMBER','1')
    shutil.rmtree(W,ignore_errors=True); os.makedirs(W); os.makedirs(OUT,exist_ok=True)
    proj=os.path.join(W,'proj')
    for ruta,txt in FILES.items(): escribir(os.path.join(proj,ruta),txt)
    escribir(os.path.join(proj,'apktool.yml'),YML%(vc,vn))
    iconos(proj)
    src=open(os.path.join(ROOT,'casa-en-orden.html'),encoding='utf-8').read()
    src=parchear(src,cfg,clave)
    m=re.subn(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^"]*">\n?','',src,count=1); src=m[0]
    src=src.replace('<style>','<style>\n'+fuentes_css(),1)
    escribir(os.path.join(proj,'assets','index.html'),src)
    jar=os.path.join(W,'apktool.jar'); urllib.request.urlretrieve(APKTOOL_URL,jar)
    run(['java','-jar',jar,'b',proj,'-o',os.path.join(W,'unsigned.apk')])
    firmar(os.path.join(W,'unsigned.apk'),os.path.join(OUT,'CasaEnOrden.apk'),os.environ.get('KEYSTORE_PEM',''))
    print('Listo:',os.path.join(OUT,'CasaEnOrden.apk'),'versionCode',vc)

if __name__=='__main__': main()
