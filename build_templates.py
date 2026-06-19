# Generates standalone, content-rich, on-brand Matomo page templates as full-width HTML files.
import os, base64
DIR=os.path.dirname(os.path.abspath(__file__))
LOGO_URI="data:image/png;base64,"+base64.b64encode(open(os.path.join(DIR,'matomo-logo.png'),'rb').read()).decode()

CSS = """
:root{--navy:#15163a;--navy2:#23234e;--teal:#0f8a7e;--teal-bright:#16b3a3;--teal-soft:#e3f7f3;--ink:#1c1d3e;--muted:#55566f;--muted2:#7d7e93;--line:#ebedf3;--bg:#fbfcff;--bg2:#f4f7fb;}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:#fff;line-height:1.65;-webkit-font-smoothing:antialiased;}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px;}
a{color:var(--teal);text-decoration:none;}
h1,h2,h3{font-weight:600;letter-spacing:-.02em;color:var(--navy);line-height:1.2;}
h1{font-size:46px;}h2{font-size:32px;}h3{font-size:20px;}
p{font-size:17px;color:var(--muted);}
.eyebrow{display:inline-block;font-size:13px;font-weight:600;color:var(--teal);background:var(--teal-soft);padding:6px 14px;border-radius:30px;letter-spacing:.01em;}
.btn{display:inline-block;font-weight:600;font-size:15px;padding:14px 28px;border-radius:10px;cursor:pointer;border:1.5px solid transparent;transition:transform .12s;}
.btn:active{transform:scale(.98);}
.btn-navy{background:var(--navy);color:#fff;}
.btn-teal{background:var(--teal-bright);color:#06231f;}
.btn-ghost{background:#fff;color:var(--navy);border-color:#dcdce6;}
.btn-light{background:#fff;color:var(--navy);}
nav.site{position:sticky;top:0;z-index:50;background:rgba(21,22,58,.97);backdrop-filter:blur(8px);color:#fff;}
nav.site .wrap{display:flex;align-items:center;justify-content:space-between;height:64px;position:relative;}
.logo{font-size:22px;font-weight:600;display:flex;align-items:center;gap:8px;letter-spacing:-.02em;}
.logo .dot{color:var(--teal-bright);}
.logo-img{height:28px;display:block;}
.navlinks{display:flex;align-items:center;gap:6px;font-size:14px;}
.navlinks>a{color:#c2c2d6;padding:0 12px;}
.navlinks>a:hover{color:#fff;}
.navitem{position:relative;display:flex;align-items:center;height:64px;}
.navitem>.top{display:flex;align-items:center;gap:5px;cursor:pointer;color:#c2c2d6;padding:0 12px;}
.navitem:hover>.top{color:#fff;}
.navitem .chev{font-size:13px;transition:transform .16s;display:inline-block;}
.navitem:hover .chev{transform:rotate(180deg);}
.mega{position:absolute;top:62px;left:0;background:#fff;border:1px solid var(--line);border-radius:14px;box-shadow:0 26px 64px -18px rgba(21,22,58,.34);padding:26px 30px;display:flex;flex-wrap:nowrap;gap:30px;width:max-content;max-width:calc(100vw - 40px);opacity:0;visibility:hidden;transform:translateY(8px);transition:opacity .16s,transform .16s,visibility .16s;z-index:60;}
.mega.right{left:auto;right:0;}
.mega.center{left:50%;right:auto;transform:translateX(-50%) translateY(8px);}
.mega.m4{flex-wrap:wrap;width:432px;column-gap:36px;row-gap:24px;}
.navitem:hover .mega{opacity:1;visibility:visible;transform:translateY(0);}
.navitem:hover .mega.center{transform:translateX(-50%) translateY(0);}
.megacol{min-width:160px;}
.mega.m4 .megacol{min-width:0;width:calc(50% - 18px);}
.megacol h5{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--muted2);margin-bottom:12px;}
.megacol a{display:block;color:var(--ink);font-size:14px;font-weight:500;padding:7px 0;border:none;}
.megacol a:hover{color:var(--teal);}
.megacol a.more{color:var(--teal);font-weight:600;}
.megafeat{background:linear-gradient(135deg,#15163a,#123f3b);border-radius:12px;padding:20px;width:210px;color:#fff;display:flex;flex-direction:column;justify-content:center;}
.megafeat b{font-size:14px;color:#fff;display:block;margin-bottom:8px;}
.megafeat .pl{display:inline-block;font-size:11px;background:rgba(255,255,255,.1);color:#dcdcec;border-radius:20px;padding:4px 10px;margin:3px 3px 0 0;}
.navcta{display:flex;align-items:center;gap:18px;}
.navcta .util{font-size:14px;color:#c2c2d6;display:inline-flex;align-items:center;gap:5px;cursor:pointer;}
.navcta .util:hover{color:#fff;}
.navcta .util .ti{font-size:15px;}
.hero{background:linear-gradient(180deg,var(--bg) 0%,var(--bg2) 100%);padding:90px 0 80px;text-align:center;}
.hero h1{max-width:780px;margin:22px auto 22px;}
.hero p.lead{font-size:20px;max-width:560px;margin:0 auto 34px;line-height:1.55;}
.hero-cta{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:18px;}
.microcopy{font-size:13px;color:var(--muted2);}
.section{padding:80px 0;}
.section.alt{background:var(--bg2);}
.section.dark{background:var(--navy);color:#fff;}
.section.dark h2,.section.dark h3{color:#fff;}
.section.dark p{color:#b9b9d0;}
.center{text-align:center;}
.sec-head{max-width:620px;margin:0 auto 48px;text-align:center;}
.sec-head p{font-size:18px;margin-top:12px;}
.grid{display:grid;gap:22px;}
.g3{grid-template-columns:repeat(3,1fr);}
.g2{grid-template-columns:repeat(2,1fr);}
.g4{grid-template-columns:repeat(4,1fr);}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:28px;}
.card .ic{width:48px;height:48px;border-radius:13px;background:var(--teal-soft);display:flex;align-items:center;justify-content:center;font-size:24px;color:var(--teal);margin-bottom:16px;}
.card h3{font-size:18px;margin-bottom:8px;}
.card p{font-size:15px;line-height:1.6;}
.prose{max-width:760px;margin:0 auto;}
.prose h2{margin:44px 0 16px;}
.prose h3{margin:32px 0 12px;}
.prose p{margin-bottom:18px;font-size:17px;color:#3c3d5a;}
.prose ul{margin:0 0 22px 22px;color:#3c3d5a;font-size:17px;}
.prose li{margin-bottom:8px;}
.shot{border-radius:18px;border:1px solid var(--line);background:var(--bg2);height:360px;display:flex;align-items:center;justify-content:center;color:#aeb0c0;gap:8px;font-size:15px;}
.steps{max-width:640px;margin:0 auto;display:flex;flex-direction:column;gap:22px;}
.step{display:flex;gap:18px;align-items:flex-start;}
.step .n{flex:none;width:36px;height:36px;border-radius:50%;background:var(--teal-soft);color:var(--teal);font-weight:600;display:flex;align-items:center;justify-content:center;}
.step p{margin:0;font-size:15px;}
.pill{display:inline-block;background:var(--navy2);border:1px solid #34345e;color:#dcdcec;padding:8px 16px;border-radius:30px;font-size:13px;margin:4px;}
.cmp2-wrap{max-width:880px;margin:0 auto;}
.cmp2{width:100%;border-collapse:separate;border-spacing:0;}
.cmp2 th,.cmp2 td{padding:16px 26px;text-align:left;vertical-align:middle;}
.cmp2 .col-crit{width:50%;}
.cmp2 .col-mat,.cmp2 .col-comp{text-align:center;}
.cmp2 thead th{font-size:16px;font-weight:600;color:var(--navy);padding-top:20px;padding-bottom:20px;}
.cmp2 thead .col-comp{color:var(--muted);font-weight:600;}
.cmp2 thead .col-mat{vertical-align:top;}
.cmp2 .mat-logo{display:block;font-size:19px;font-weight:700;color:var(--navy);letter-spacing:-.02em;}
.cmp2 .rec{display:inline-block;font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#06231f;background:var(--teal-bright);border-radius:20px;padding:3px 11px;margin-top:7px;}
.cmp2 td.col-mat,.cmp2 th.col-mat{background:var(--teal-soft);}
.cmp2 thead th.col-mat{border-top-left-radius:16px;border-top-right-radius:16px;}
.cmp2 tbody tr:last-child td.col-mat{border-bottom-left-radius:16px;border-bottom-right-radius:16px;}
.cmp2 tbody td{font-size:15.5px;color:#33344f;border-bottom:1px solid var(--line);}
.cmp2 tbody td.col-crit{font-weight:500;}
.cmp2 tbody tr:last-child td{border-bottom:none;}
.ck{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;}
.ck.yes{background:var(--teal-bright);box-shadow:0 2px 7px rgba(15,138,126,.32);}
.ck.no{background:#dfe2ee;}
.pp{display:inline-block;font-size:12px;font-weight:600;color:#9a6c12;background:#fbeecb;border-radius:20px;padding:5px 13px;}
@media(max-width:760px){.cmp2-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--line);border-radius:14px;}.cmp2{min-width:540px;}.cmp2 th,.cmp2 td{padding:13px 16px;}}
.yes{color:var(--teal);font-weight:600;}.no{color:#c45b54;font-weight:600;}.part{color:#c99a3a;font-size:13px;}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;}
.stat{background:var(--bg2);border-radius:14px;padding:26px;text-align:center;}
.stat .big{font-size:34px;font-weight:600;color:var(--teal);letter-spacing:-.02em;}
.stat p{font-size:14px;margin-top:6px;}
.callout{background:var(--teal-soft);border-radius:20px;padding:56px 40px;text-align:center;}
.callout h2{margin-bottom:12px;}.callout p{color:#3f6b62;max-width:420px;margin:0 auto 26px;font-size:17px;}
.faq{max-width:760px;margin:0 auto;}
.faq details{border:1px solid var(--line);border-radius:12px;margin-bottom:12px;padding:18px 22px;}
.faq summary{font-size:16px;font-weight:600;color:var(--navy);cursor:pointer;list-style:none;display:flex;justify-content:space-between;}
.faq summary::-webkit-details-marker{display:none;}
.faq p{margin-top:12px;font-size:15px;color:#3c3d5a;}
.quote{border-left:3px solid var(--teal-bright);padding:6px 0 6px 22px;max-width:680px;margin:0 auto;}
.quote p{font-size:20px;font-style:italic;color:#2b2c4d;line-height:1.55;font-family:Georgia,serif;margin-bottom:10px;}
.quote .who{font-size:14px;color:var(--muted2);font-style:normal;}
.related{background:var(--bg2);border-radius:14px;padding:22px 26px;max-width:760px;margin:30px auto 0;font-size:15px;color:var(--muted);}
.toc{background:var(--bg2);border-radius:14px;padding:22px 26px;max-width:760px;margin:0 auto 36px;}
.toc strong{display:block;margin-bottom:8px;color:var(--navy);}
.toc a{display:block;padding:4px 0;font-size:15px;}
.ratings{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:26px;}
.rb{display:flex;align-items:center;gap:9px;background:#fff;border:1px solid var(--line);border-radius:30px;padding:8px 17px;font-size:15px;font-weight:600;color:var(--navy);}
.rb .dot{width:18px;height:18px;border-radius:5px;display:inline-flex;align-items:center;justify-content:center;font-size:10px;color:#fff;font-weight:700;}
.rb .star{color:#f5a623;font-size:14px;}
.rb small{font-size:11px;color:var(--muted2);font-weight:600;text-transform:uppercase;letter-spacing:.03em;}
.clients{background:var(--navy);padding:36px 0 38px;}
.clients .lbl{text-align:center;color:#9fa0bb;font-size:14px;margin-bottom:24px;}
.clients .lbl b{color:#fff;font-weight:600;}
.clients .row{display:flex;align-items:center;justify-content:center;gap:46px;flex-wrap:wrap;}
.clients .lg{color:#c9cadd;font-size:19px;font-weight:600;letter-spacing:.05em;opacity:.82;}
.learn{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;}
.lcard{border:1px solid var(--line);border-radius:18px;overflow:hidden;display:flex;flex-direction:column;background:#fff;transition:transform .12s,box-shadow .12s;}
.lcard:hover{transform:translateY(-3px);box-shadow:0 12px 32px rgba(21,22,58,.09);}
.lcard .img{height:172px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:34px;}
.lcard .pad{padding:20px 22px 22px;display:flex;flex-direction:column;flex:1;}
.lcard .lt{font-size:12px;font-weight:600;color:var(--teal);text-transform:uppercase;letter-spacing:.04em;margin-bottom:9px;}
.lcard h3{font-size:19px;margin-bottom:9px;line-height:1.28;}
.lcard p{font-size:14.5px;color:var(--muted);line-height:1.6;flex:1;margin:0;}
.lcard .rl{margin-top:16px;font-weight:600;font-size:14.5px;color:var(--navy);display:inline-flex;align-items:center;gap:6px;}
@media(max-width:860px){.learn{grid-template-columns:1fr 1fr;}}@media(max-width:560px){.learn{grid-template-columns:1fr;}}
.vsband{background:linear-gradient(130deg,#15163a 0%,#123f3b 100%);color:#fff;padding:88px 0;position:relative;overflow:hidden;}
.vsband::before{content:"VS";position:absolute;top:-30px;right:40px;font-size:220px;font-weight:800;color:rgba(255,255,255,.04);letter-spacing:-.05em;line-height:1;pointer-events:none;}
.vsband .head{text-align:center;max-width:660px;margin:0 auto 46px;position:relative;}
.vsband .eyebrow{background:rgba(22,179,163,.18);color:var(--teal-bright);}
.vsband h2{color:#fff;font-size:36px;margin-top:18px;}
.vsband .head p{color:#c4c5dd;font-size:18px;margin-top:14px;}
.vsgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;position:relative;}
.vscard{background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:24px 22px;display:flex;flex-direction:column;gap:13px;transition:transform .14s,background .14s,border-color .14s;}
.vscard:hover{transform:translateY(-4px);background:rgba(255,255,255,.1);border-color:rgba(22,179,163,.5);}
.vsmatch{display:flex;align-items:center;gap:9px;font-size:16px;font-weight:600;}
.vsmatch .m{color:var(--teal-bright);}
.vsmatch .x{font-size:11px;font-weight:700;letter-spacing:.1em;color:#7d7e9a;background:rgba(255,255,255,.08);border-radius:6px;padding:3px 7px;}
.vsmatch .o{color:#dcdcec;}
.vscard p{color:#a9aac6;font-size:14px;line-height:1.55;margin:0;flex:1;}
.vscard .go{color:var(--teal-bright);font-weight:600;font-size:14px;display:inline-flex;align-items:center;gap:6px;}
@media(max-width:860px){.vsgrid{grid-template-columns:1fr 1fr;}.vsband h2{font-size:28px;}}
@media(max-width:560px){.vsgrid{grid-template-columns:1fr;}}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;max-width:1120px;margin:0 auto;}
.frow>.ftext,.frow>.fvisual{min-width:0;}
.frow.rev .ftext{order:2;}
.feyebrow{font-size:15px;color:var(--muted2);font-weight:500;margin-bottom:14px;}
.ftext h2{font-size:40px;line-height:1.12;margin-bottom:20px;}
.ftext>p{font-size:17px;color:var(--muted);margin-bottom:24px;line-height:1.6;}
.flist{list-style:none;margin:0 0 30px;padding:0;}
.flist li{position:relative;padding-left:28px;margin-bottom:15px;font-size:16px;color:#3c3d5a;line-height:1.55;}
.flist li::before{content:"";position:absolute;left:3px;top:8px;width:8px;height:8px;border-radius:50%;background:var(--teal-bright);}
.fbtn{display:inline-block;border:1.5px solid var(--navy);color:var(--navy);border-radius:32px;padding:13px 32px;font-weight:600;font-size:15px;transition:background .14s,color .14s;}
.fbtn:hover{background:var(--navy);color:#fff;}
.mock{border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:0 24px 60px -16px rgba(21,22,58,.28);background:#fff;max-width:100%;}
.mockbar{display:flex;align-items:center;gap:7px;padding:12px 15px;background:var(--bg2);border-bottom:1px solid var(--line);}
.mockbar em{width:11px;height:11px;border-radius:50%;display:inline-block;font-style:normal;}
.mockbar em:nth-child(1){background:#ff5f57;}.mockbar em:nth-child(2){background:#febc2e;}.mockbar em:nth-child(3){background:#28c840;}
.mockbar .url{margin-left:12px;font-size:12px;color:var(--muted2);background:#fff;border:1px solid var(--line);border-radius:7px;padding:4px 14px;flex:1;}
.mockbody{position:relative;padding:26px 28px;min-height:300px;}
.hm .bar{height:34px;border-radius:8px;background:#e9ebf3;margin-bottom:22px;}
.hm .ln{height:11px;border-radius:6px;background:#edeff6;margin-bottom:13px;}
.hm .ln.s{width:52%;}.hm .ln.m{width:78%;}.hm .ln.l{width:92%;}
.hm .cta{display:inline-block;margin-top:10px;background:#dde1ee;border-radius:9px;padding:15px 46px;}
.blob{position:absolute;border-radius:50%;pointer-events:none;mix-blend-mode:multiply;}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:20px;}
.tile{border:1px solid var(--line);border-radius:10px;padding:12px 13px;}
.tile span.tl{font-size:10.5px;color:var(--muted2);display:block;margin-bottom:6px;}
.tile b{font-size:19px;color:var(--navy);}
.tile i{font-size:11px;font-style:normal;margin-left:5px;}
.tile i.up{color:#1f9d6b;}.tile i.down{color:#d35b54;}
.chart{width:100%;height:150px;display:block;}
@media(max-width:860px){.frow{grid-template-columns:1fr;gap:36px;}.frow.rev .ftext{order:0;}.ftext h2{font-size:30px;}}
.tmgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;}
.tm{background:#fff;border:1px solid var(--line);border-radius:16px;padding:26px 26px 24px;display:flex;flex-direction:column;box-shadow:0 6px 20px -12px rgba(21,22,58,.16);}
.tm .stars{color:#f5a623;font-size:15px;letter-spacing:2px;margin-bottom:13px;}
.tm .q{font-size:15px;color:#33344f;line-height:1.62;flex:1;margin:0 0 18px;}
.tm .who{display:flex;align-items:center;gap:12px;}
.tm .who .av{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#16b3a3,#15163a);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:15px;flex:none;}
.tm .who b{display:block;font-size:14px;color:var(--navy);}
.tm .who span{font-size:12.5px;color:var(--muted2);}
@media(max-width:860px){.tmgrid{grid-template-columns:1fr;}}
.mlgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;}
.ml{display:flex;flex-direction:column;gap:9px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;transition:transform .12s,border-color .12s;}
.ml:hover{transform:translateY(-3px);border-color:var(--teal-bright);}
.ml .mic{width:40px;height:40px;border-radius:11px;background:var(--teal-soft);color:var(--teal);display:flex;align-items:center;justify-content:center;font-size:21px;}
.ml h3{font-size:15.5px;margin:0;}
.ml p{font-size:13px;color:var(--muted);margin:0;line-height:1.5;flex:1;}
.ml .go{font-size:13px;font-weight:600;color:var(--teal);display:inline-flex;align-items:center;gap:5px;margin-top:3px;}
@media(max-width:860px){.mlgrid{grid-template-columns:1fr 1fr;}}
@media(max-width:560px){.mlgrid{grid-template-columns:1fr;}}
.cmp2 tr.cat td{background:var(--bg2);font-size:11.5px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--muted2);padding-top:13px;padding-bottom:13px;}
.cmp2 tr.cat td.col-mat{background:#d6f3ee;}
.byline{display:flex;align-items:center;gap:13px;margin-top:24px;}
.byline .avatar{width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,#16b3a3,#15163a);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:16px;flex:none;}
.byline .bmeta{font-size:14.5px;line-height:1.45;}
.byline .bmeta b{color:var(--navy);font-weight:600;}
.byline .bmeta span{color:var(--muted2);display:block;font-size:13px;}
.article{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:56px;align-items:start;max-width:1080px;margin:0 auto;}
.asidebar{position:sticky;top:88px;display:flex;flex-direction:column;gap:18px;}
.inbrief{background:linear-gradient(135deg,#15163a,#123f3b);color:#fff;border-radius:18px;padding:30px 32px;margin-bottom:36px;}
.inbrief h3{color:#fff;font-size:14px;text-transform:uppercase;letter-spacing:.07em;display:flex;align-items:center;gap:9px;margin-bottom:18px;}
.inbrief h3 i{color:var(--teal-bright);font-size:18px;}
.inbrief ul{list-style:none;margin:0;padding:0;}
.inbrief li{position:relative;padding-left:26px;margin-bottom:13px;font-size:15.5px;color:#dde0f0;line-height:1.55;}
.inbrief li::before{content:"";position:absolute;left:3px;top:8px;width:7px;height:7px;border-radius:50%;background:var(--teal-bright);}
.inbrief li:last-child{margin-bottom:0;}
.sidecta{background:#fff;border:1px solid var(--line);border-radius:16px;padding:24px 22px;box-shadow:0 10px 30px -14px rgba(21,22,58,.18);}
.sidecta.dark{background:var(--navy);border:none;color:#fff;}
.sidecta .st{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--teal);margin-bottom:9px;}
.sidecta.dark .st{color:var(--teal-bright);}
.sidecta h4{font-size:19px;color:var(--navy);margin-bottom:8px;line-height:1.25;}
.sidecta.dark h4{color:#fff;}
.sidecta p{font-size:14px;color:var(--muted);margin-bottom:16px;line-height:1.55;}
.sidecta.dark p{color:#b9b9d0;}
.sidecta .btn{display:block;width:100%;text-align:center;padding:12px 0;}
.sideform{display:flex;flex-direction:column;gap:9px;}
.sideform input{min-width:0;}
@media(max-width:560px){.sideform{flex-direction:column!important;}}
.sideform input{border:1px solid var(--line);border-radius:9px;padding:11px 13px;font-size:14px;font-family:inherit;color:var(--ink);}
.sideform input:focus{outline:none;border-color:var(--teal-bright);}
.sidelist{list-style:none;margin:0;padding:0;}
.sidelist li{border-top:1px solid var(--line);}
.sidelist li:first-child{border-top:none;}
.sidelist a{display:flex;align-items:center;gap:10px;padding:11px 0;font-size:14px;color:var(--navy);font-weight:500;}
.sidelist a i{color:var(--teal);font-size:18px;}
.authorbox{display:flex;gap:22px;align-items:flex-start;background:var(--bg2);border:1px solid var(--line);border-radius:18px;padding:30px 32px;max-width:700px;margin:0;}
.authorbox .avatar{width:72px;height:72px;border-radius:50%;background:linear-gradient(135deg,#16b3a3,#15163a);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:26px;flex:none;}
.authorbox .ainfo h4{font-size:18px;margin-bottom:3px;}
.authorbox .ainfo .role{font-size:13px;color:var(--teal);font-weight:600;margin-bottom:11px;}
.authorbox .ainfo p{font-size:14.5px;color:var(--muted);line-height:1.6;margin-bottom:15px;}
.authorbox .social{display:flex;gap:10px;}
.authorbox .social a{width:34px;height:34px;border-radius:9px;background:#fff;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--navy);font-size:17px;}
.authorbox .social a:hover{background:var(--navy);color:#fff;border-color:var(--navy);}
@media(max-width:960px){.article{grid-template-columns:1fr;}.asidebar{position:static;flex-direction:row;flex-wrap:wrap;}.asidebar>*{flex:1;min-width:240px;}}
@media(max-width:560px){.authorbox{flex-direction:column;}.asidebar{flex-direction:column;}}
.anno{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:50%;background:var(--teal-bright);color:#fff;font-size:12px;font-weight:700;font-style:italic;font-family:Georgia,serif;cursor:pointer;vertical-align:middle;margin-left:8px;border:none;box-shadow:0 2px 6px rgba(15,138,126,.45);transition:transform .12s;line-height:1;padding:0;}
.anno:hover{transform:scale(1.18);}
.anno-overlay{position:fixed;inset:0;background:rgba(15,16,40,.5);backdrop-filter:blur(7px);-webkit-backdrop-filter:blur(7px);z-index:300;display:flex;align-items:center;justify-content:center;padding:24px;opacity:0;pointer-events:none;transition:opacity .22s;}
.anno-overlay.show{opacity:1;pointer-events:auto;}
.anno-card{background:#fff;border-radius:18px;max-width:450px;width:100%;padding:32px 34px;box-shadow:0 34px 90px rgba(21,22,58,.42);transform:translateY(12px) scale(.98);transition:transform .22s;position:relative;border-top:4px solid var(--teal-bright);}
.anno-overlay.show .anno-card{transform:translateY(0) scale(1);}
.anno-card .tag{display:inline-flex;align-items:center;gap:7px;font-size:11.5px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--teal);margin-bottom:13px;}
.anno-card h4{font-size:20px;color:var(--navy);margin-bottom:11px;line-height:1.25;}
.anno-card p{font-size:15px;color:var(--muted);line-height:1.62;margin:0;}
.anno-card .x{position:absolute;top:16px;right:18px;width:30px;height:30px;border-radius:50%;border:none;background:var(--bg2);color:var(--muted);cursor:pointer;font-size:15px;display:flex;align-items:center;justify-content:center;line-height:1;}
.anno-card .x:hover{background:var(--line);color:var(--navy);}
.anno-hint{position:fixed;left:18px;bottom:18px;z-index:150;background:#fff;border:1px solid var(--line);box-shadow:0 8px 26px rgba(21,22,58,.15);border-radius:30px;padding:9px 17px 9px 11px;font-size:13px;color:var(--muted);display:flex;align-items:center;gap:9px;}
.anno-hint b{display:inline-flex;width:20px;height:20px;border-radius:50%;background:var(--teal-bright);color:#fff;align-items:center;justify-content:center;font-size:12px;font-family:Georgia,serif;font-weight:700;font-style:italic;}
@media(max-width:560px){.anno-hint{display:none;}}
.backhub{position:fixed;right:18px;bottom:18px;z-index:150;background:var(--navy);color:#fff;border:none;box-shadow:0 8px 26px rgba(21,22,58,.26);border-radius:30px;padding:10px 18px;font-size:13px;font-weight:600;display:inline-flex;align-items:center;gap:7px;}
.backhub:hover{background:var(--navy2);color:#fff;}
@media(max-width:560px){.backhub{padding:9px 14px;}}
.cbadge{display:inline-block;font-size:12.5px;font-weight:600;color:var(--teal);background:#fff;border:1px solid #bfeee8;border-radius:20px;padding:6px 14px;}
.ownrow{display:flex;align-items:center;gap:14px;border-radius:12px;padding:15px 17px;margin-bottom:12px;}
.ownrow:last-child{margin-bottom:0;}
.ownrow.good{background:var(--teal-soft);border:1px solid #bfeee8;}
.ownrow.badrow{background:#f4f5f9;border:1px solid var(--line);}
.ownrow .oic{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex:none;}
.ownrow.good .oic{background:var(--teal-bright);color:#fff;}
.ownrow.badrow .oic{background:#dfe2ee;color:#8a8ca6;}
.ownrow b{display:block;font-size:15px;color:var(--navy);}
.ownrow .od{font-size:13px;color:var(--muted);}
.ownrow .otag{margin-left:auto;font-size:11.5px;font-weight:600;border-radius:20px;padding:5px 12px;white-space:nowrap;}
.ownrow.good .otag{background:var(--teal-bright);color:#06231f;}
.ownrow.badrow .otag{background:#e2e4ee;color:#7d7e93;}
.bcat{display:flex;flex-wrap:wrap;gap:9px;justify-content:center;margin-bottom:50px;}
.bcat a{font-size:13.5px;font-weight:500;color:var(--muted);background:#fff;border:1px solid var(--line);border-radius:30px;padding:8px 16px;cursor:pointer;transition:background .12s,color .12s,border-color .12s;}
.bcat a.active,.bcat a:hover{background:var(--navy);color:#fff;border-color:var(--navy);}
.pager{display:flex;justify-content:center;align-items:center;gap:8px;margin-top:46px;}
.pager a{min-width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center;border:1px solid var(--line);border-radius:10px;font-size:14px;font-weight:600;color:var(--navy);background:#fff;padding:0 12px;transition:border-color .12s,color .12s,background .12s;}
.pager a:hover{border-color:var(--teal-bright);color:var(--teal);}
.pager a.active{background:var(--navy);color:#fff;border-color:var(--navy);}
.pager a.nav{color:var(--muted);}
.pager a.nav:hover{color:var(--teal);}
.pager .dots{color:var(--muted2);padding:0 4px;}
.feat{display:grid;grid-template-columns:1.05fr 1fr;background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;margin-bottom:56px;box-shadow:0 14px 40px -18px rgba(21,22,58,.2);}
.feat .img{min-height:340px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:46px;}
.feat .fbody{padding:42px 44px;display:flex;flex-direction:column;justify-content:center;}
.feat .ftag{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;color:var(--teal);margin-bottom:13px;}
.feat h2{font-size:29px;line-height:1.18;margin-bottom:14px;}
.feat .fx{font-size:16px;color:var(--muted);margin-bottom:22px;line-height:1.6;}
.pmeta{display:flex;align-items:center;gap:11px;font-size:13px;color:var(--muted2);}
.pmeta .av{width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,#16b3a3,#15163a);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:13px;flex:none;}
.pmeta b{color:var(--navy);font-weight:600;}
.postgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;}
.post{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;transition:transform .12s,box-shadow .12s;}
.post:hover{transform:translateY(-4px);box-shadow:0 16px 38px rgba(21,22,58,.11);}
.post .img{height:152px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:30px;}
.post .pbody{padding:20px 22px 22px;display:flex;flex-direction:column;flex:1;}
.post .ptag{font-size:11.5px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;color:var(--teal);margin-bottom:9px;}
.post h3{font-size:17px;line-height:1.3;margin-bottom:9px;}
.post p{font-size:13.5px;color:var(--muted);line-height:1.55;flex:1;margin-bottom:16px;}
@media(max-width:860px){.feat{grid-template-columns:1fr;}.feat .img{min-height:200px;}.feat .fbody{padding:30px 28px;}.postgrid{grid-template-columns:1fr 1fr;}}
@media(max-width:560px){.postgrid{grid-template-columns:1fr;}}
.cmpcat{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--muted2);margin:40px 0 18px;}
.cmpcat.first{margin-top:0;}
.cmpgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;}
.cmpc{display:flex;flex-direction:column;gap:9px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px 24px;transition:transform .12s,border-color .12s,box-shadow .12s;}
.cmpc:hover{transform:translateY(-3px);border-color:var(--teal-bright);box-shadow:0 12px 30px rgba(21,22,58,.09);}
.cmpc .vs{font-size:17px;font-weight:600;color:var(--navy);letter-spacing:-.01em;}
.cmpc .vs span{color:var(--teal);font-weight:600;}
.cmpc p{font-size:13.5px;color:var(--muted);margin:0;line-height:1.55;flex:1;}
.cmpc .go{font-size:13.5px;font-weight:600;color:var(--teal);display:inline-flex;align-items:center;gap:6px;margin-top:3px;}
@media(max-width:860px){.cmpgrid{grid-template-columns:1fr 1fr;}}
@media(max-width:560px){.cmpgrid{grid-template-columns:1fr;}}
.fhnav{position:sticky;top:64px;z-index:40;background:rgba(255,255,255,.96);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);}
.fhnav .row{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;padding:13px 24px;max-width:1120px;margin:0 auto;}
.fhnav a{font-size:13.5px;font-weight:500;color:var(--muted);padding:7px 15px;border-radius:30px;}
.fhnav a:hover{background:var(--bg2);color:var(--navy);}
.fhcat{display:flex;align-items:baseline;gap:11px;margin:0 0 22px;}
.fhcat h2{font-size:24px;}
.fhcat .n{font-size:13px;color:var(--muted2);font-weight:600;}
.fhgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:54px;}
.fhcard{display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;transition:transform .12s,border-color .12s,box-shadow .12s;}
.fhcard:hover{transform:translateY(-3px);border-color:var(--teal-bright);box-shadow:0 12px 30px rgba(21,22,58,.09);}
.fhcard .ic{flex:none;width:42px;height:42px;border-radius:11px;background:var(--teal-soft);color:var(--teal);display:flex;align-items:center;justify-content:center;font-size:21px;}
.fhcard h3{font-size:15.5px;margin-bottom:4px;color:var(--navy);}
.fhcard p{font-size:13px;color:var(--muted);line-height:1.5;margin:0;}
@media(max-width:860px){.fhgrid{grid-template-columns:1fr 1fr;}.fhnav{display:none;}}
@media(max-width:560px){.fhgrid{grid-template-columns:1fr;}}
footer.site{background:var(--navy);color:#b9b9d0;padding:56px 0 28px;}
footer.site .cols{display:grid;grid-template-columns:repeat(5,1fr);gap:26px;font-size:13px;line-height:2;}
footer.site .cols a{display:block;color:#b9b9d0;}
footer.site h4{color:#fff;font-size:14px;font-weight:600;margin-bottom:8px;}
footer.site .base{border-top:1px solid #2c2c54;margin-top:36px;padding-top:20px;text-align:center;}
footer.site .base .tag{font-style:italic;color:#9596b0;margin-bottom:4px;}
footer.site .base .cp{font-size:12px;color:#6a6b85;}
@media(max-width:860px){h1{font-size:34px;}h2{font-size:26px;}.g3,.g4,.stats{grid-template-columns:1fr 1fr;}footer.site .cols{grid-template-columns:1fr 1fr;}.navlinks{display:none;}}
@media(max-width:560px){.g2,.g3,.g4,.stats,footer.site .cols{grid-template-columns:1fr;}.hero{padding:60px 0 50px;}}
"""

NAV = f"""<nav class="site"><div class="wrap">
<a class="logo" href="index.html"><img class="logo-img" src="{LOGO_URI}" alt="Matomo"></a>
<div class="navlinks">
<div class="navitem"><span class="top">Why Matomo <i class="ti ti-chevron-down chev"></i></span><div class="mega">
<div class="megacol"><h5>Our difference</h5><a href="#">100% data ownership</a><a href="#">Cookieless tracking</a><a href="#">No data sampling</a><a href="#">Open source</a></div>
<div class="megacol"><h5>Trust &amp; compliance</h5><a href="#">GDPR compliance</a><a href="#">Privacy by design</a><a href="#">Security</a><a class="more" href="2-vs-page-google-analytics.html">Matomo vs Google Analytics</a></div>
</div></div>
<div class="navitem"><span class="top">Product <i class="ti ti-chevron-down chev"></i></span><div class="mega">
<div class="megacol"><a href="#">Matomo Cloud</a><a href="#">Matomo On-Premise</a></div>
</div></div>
<div class="navitem"><span class="top">Features <i class="ti ti-chevron-down chev"></i></span><div class="mega center">
<div class="megacol"><h5>Measure</h5><a href="#">Web analytics</a><a href="#">Custom reports</a><a href="#">Real-time data</a></div>
<div class="megacol"><h5>Understand behaviour</h5><a href="1-feature-landing-heatmaps.html">Heatmaps</a><a href="#">Session recordings</a><a href="#">Form analytics</a></div>
<div class="megacol"><h5>Optimise &amp; convert</h5><a href="#">A/B testing</a><a href="#">Funnel analysis</a><a href="#">Goals &amp; conversions</a></div>
<div class="megacol"><h5>Collect</h5><a href="#">Tag Manager</a><a href="5-use-case-ecommerce.html">Ecommerce tracking</a><a href="#">Server-side tracking</a><a class="more" href="9-features-hub.html">See all features</a></div>
</div></div>
<div class="navitem"><span class="top">Resources <i class="ti ti-chevron-down chev"></i></span><div class="mega right">
<div class="megacol"><h5>Learn</h5><a href="7-blog-index.html">Blog</a><a href="#">Guides</a><a href="6-blog-pillar-bounce-rate.html">Glossary</a><a href="#">Newsletter</a></div>
<div class="megacol"><h5>Support</h5><a href="#">Help center</a><a href="#">FAQ</a><a href="#">Documentation</a><a href="#">Case studies</a></div>
</div></div>
<a href="#">Pricing</a>
</div>
<div class="navcta"><a class="util"><i class="ti ti-world"></i> EN</a><a class="util">Help</a><a class="util">Log in</a><a class="btn btn-teal" style="padding:9px 16px;">Try it for free</a></div>
</div></nav>"""

FOOTER = """<footer class="site"><div class="wrap">
<div class="cols">
<div><h4>Product</h4><a>Web analytics</a><a>Heatmaps</a><a>Session recordings</a><a>A/B testing</a><a>Funnels</a><a>Tag Manager</a></div>
<div><h4>Why Matomo</h4><a>100% data ownership</a><a>GDPR</a><a>Cookieless</a><a>Open source</a><a>No data sampling</a></div>
<div><h4>Resources</h4><a>Blog</a><a>Guides</a><a>Case studies</a><a>Newsletter</a><a>Help centre</a></div>
<div><h4>Compare</h4><a>vs Google Analytics</a><a>vs Hotjar</a><a>vs Plausible</a><a>vs Amplitude</a><a>vs Piwik PRO</a></div>
<div><h4>Company</h4><a>About</a><a>History</a><a>Hiring</a><a>Contact</a><a>Partners</a></div>
</div>
<div class="base"><p class="tag">Built on open source. Governed by ethics. Powered by insight.</p><p class="cp">© 2026 Analytics Platform, Matomo</p></div>
</div></footer>"""

ANNO_JS="""<div class="anno-overlay" id="annoOv"><div class="anno-card"><button class="x" id="annoX" aria-label="Close">✕</button><div class="tag">◉ Why we made this choice</div><h4 id="annoTitle"></h4><p id="annoBody"></p></div></div>
<div class="anno-hint"><b>i</b> Click the markers to see the SEO rationale</div>
<a class="backhub" href="index.html"><i class="ti ti-arrow-left"></i> All templates</a>
<script>(function(){var ov=document.getElementById('annoOv'),tt=document.getElementById('annoTitle'),bd=document.getElementById('annoBody');document.querySelectorAll('.anno').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();tt.textContent=a.getAttribute('data-title')||'Why we made this choice';bd.innerHTML=a.getAttribute('data-note')||'';ov.classList.add('show');});});function c(){ov.classList.remove('show');}document.getElementById('annoX').addEventListener('click',c);ov.addEventListener('click',function(e){if(e.target===ov)c();});document.addEventListener('keydown',function(e){if(e.key==='Escape')c();});})();</script>"""

def shell(title, desc, body):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@2.47.0/dist/tabler-icons.min.css" rel="stylesheet">
<style>{CSS}</style></head><body>{NAV}{body}{FOOTER}{ANNO_JS}</body></html>"""

def anno(note,title="Why we made this choice"):
    n=note.replace('"','&quot;')
    return f'<button class="anno" type="button" data-title="{title}" data-note="{n}" aria-label="{title}">i</button>'

# Strategic rationale notes (client-facing, English)
A_MAILLAGE=anno("These related articles are not decorative. They build internal links between pages of the same <b>topic cluster (semantic cocoon)</b>, so topical authority and link equity flow between them and visitors stay longer. Internal linking is one of the strongest on-page SEO levers.","Internal linking &middot; topic cluster")
A_VS=anno("This block links to our <b>comparison (VS) pages</b> inside the same topic cluster and captures high-intent <b>'alternative / vs'</b> searches. It positions Matomo as the category leader exactly where buyers compare options.","Comparison block &amp; internal linking")
A_FAQ=anno("The FAQ targets <b>long-tail and 'People Also Ask'</b> queries, makes the page eligible for <b>FAQ rich results</b> in Google, and answers buying objections, all of which lift both rankings and conversion.","Why an FAQ")
A_RATINGS=anno("Showing real ratings from G2, Capterra and GetApp is a <b>trust and reassurance</b> signal that reinforces <b>E-E-A-T</b> (experience, expertise, authoritativeness, trust), which Google rewards and which lifts conversion rate.","Review ratings &middot; E-E-A-T")
A_CLIENTS=anno("Recognisable client logos are a <b>credibility (E-E-A-T)</b> signal. They reassure visitors that Matomo is trusted by major organisations, which reduces bounce and increases conversions.","Client logos &middot; trust")
A_AUTHOR=anno("A named author with a real bio and credentials is a core <b>E-E-A-T</b> signal for content. It shows genuine expertise behind the article and builds reader trust, which Google increasingly weights for ranking.","Author box &middot; E-E-A-T")
A_INBRIEF=anno("This summary is <b>featured-snippet bait</b>: a concise, structured answer Google can lift into position zero. It also improves UX and lowers bounce by giving the key answer up front.","Key-takeaways box")
A_SIDECTA=anno("A sticky sidebar keeps a <b>lead-capture CTA</b> in view throughout the read, converting engaged readers into trials and subscribers without interrupting the article.","Sticky lead-capture CTAs")
A_CMP=anno("A clear comparison table captures <b>'Matomo vs ...' intent</b>, can win the comparison SERP feature, and gives a fast, scannable decision aid that favours Matomo while staying honest (note we still credit where the competitor wins).","Comparison table")
A_HERO=anno("The whole header is engineered to rank <b>and</b> convert at once: a <b>keyword-first, SEO-optimised H1</b> targeting the page's main search term, a primary <b>CTA</b> to start the trial, and <b>review ratings</b> for instant social proof, all above the fold.","Optimised landing header")
A_FROW=anno("These alternating text-and-visual sections add the <b>in-depth, keyword-rich content</b> Google needs to rank the page, while the visuals keep it engaging. Thin landing pages rarely rank, this is where the page earns its keywords.","SEO content block")
A_CALLOUT=anno("A closing call-to-action gives the now-convinced visitor <b>one last, frictionless push to start a free trial</b>. Repeating the CTA at the end of the page is one of the simplest, highest-impact conversion-rate levers.","Final conversion CTA")
A_KEEPCMP=anno("These links mesh the <b>comparison pages of the same template</b> together (vs Piwik PRO, vs Plausible, alternatives, migration). It spreads link equity across the comparison cluster and keeps high-intent visitors exploring options where Matomo wins.","Internal linking &middot; same template")

RATINGS = f"""<div class="ratings">
<span class="rb"><span class="dot" style="background:#ff4f42;">C</span>Capterra <span class="star">★</span>4.7 <small>· 62 reviews</small></span>
<span class="rb"><span class="dot" style="background:#ff492c;">G2</span>G2 <span class="star">★</span>4.2</span>
<span class="rb"><span class="dot" style="background:#1f8fe0;">G</span>GetApp <span class="star">★</span>4.7</span>{A_RATINGS}
</div>"""
CLIENTS = f"""<section class="clients"><div class="wrap">
<p class="lbl">Trusted by <b>1 million</b> websites and organisations <b>worldwide</b>{A_CLIENTS}</p>
<div class="row"><span class="lg">EUROPEAN COMMISSION</span><span class="lg">UNITED NATIONS</span><span class="lg">NHS</span><span class="lg">AMNESTY INTERNATIONAL</span><span class="lg">AHREFS</span></div>
</div></section>"""
def hero(eyebrow,h1,lead,cta1,cta2,micro,ratings=False):
    rt=RATINGS if ratings else ""
    hn=A_HERO if ratings else ""
    return f"""<section class="hero"><div class="wrap">
<span class="eyebrow">{eyebrow}</span><h1>{h1}{hn}</h1><p class="lead">{lead}</p>
<div class="hero-cta"><a class="btn btn-navy">{cta1}</a><a class="btn btn-ghost">{cta2}</a></div>
<p class="microcopy">{micro}</p>{rt}</div></section>"""

def faq(items):
    rows="".join(f'<details><summary>{q}<i class="ti ti-chevron-down"></i></summary><p>{a}</p></details>' for q,a in items)
    return f'<section class="section"><div class="wrap"><div class="sec-head"><h2>Frequently asked questions{A_FAQ}</h2></div><div class="faq">{rows}</div></div></section>'

def callout(h2,p,btn):
    return f'<section class="section"><div class="wrap"><div class="callout"><h2>{h2}{A_CALLOUT}</h2><p>{p}</p><a class="btn btn-navy">{btn}</a></div></div></section>'

shot=lambda label:f'<section class="section" style="padding-top:0;"><div class="wrap"><div class="shot"><i class="ti ti-photo" style="font-size:20px;"></i> {label}</div></div></section>'

GRADS=["linear-gradient(135deg,#16b3a3,#15163a)","linear-gradient(135deg,#7b6ef0,#d8527c)","linear-gradient(135deg,#1f8fe0,#16b3a3)"]
def learnmore(cards):
    # cards = list of (icon, tag, title, desc, cta)
    inner=""
    for i,(icon,tag,title,desc,cta) in enumerate(cards):
        inner+=f'<a class="lcard" href="#"><div class="img" style="background:{GRADS[i%3]};"><i class="ti {icon}"></i></div><div class="pad"><span class="lt">{tag}</span><h3>{title}</h3><p>{desc}</p><span class="rl">{cta} <i class="ti ti-arrow-right"></i></span></div></a>'
    return f'<section class="section alt"><div class="wrap"><div class="sec-head"><h2>Learn more{A_MAILLAGE}</h2><p>Go deeper on the topic with our guides and resources.</p></div><div class="learn">{inner}</div></div></section>'

def vsband(eyebrow,h2,sub,items):
    # items = list of (competitor, blurb)
    cards="".join(f'<a class="vscard" href="#"><div class="vsmatch"><span class="m">Matomo</span><span class="x">VS</span><span class="o">{c}</span></div><p>{b}</p><span class="go">See the comparison <i class="ti ti-arrow-right"></i></span></a>' for c,b in items)
    return f'<section class="vsband"><div class="wrap"><div class="head"><span class="eyebrow">{eyebrow}</span><h2>{h2}{A_VS}</h2><p>{sub}</p></div><div class="vsgrid">{cards}</div></div></section>'

def frow(eyebrow,h2,lead,bullets,cta,visual,rev=False,alt=False,note=False):
    lis="".join(f'<li>{b}</li>' for b in bullets)
    btn=f'<a class="fbtn">{cta}</a>' if cta else ''
    nt=A_FROW if note else ""
    text=f'<div class="ftext"><p class="feyebrow">{eyebrow}</p><h2>{h2}{nt}</h2><p>{lead}</p><ul class="flist">{lis}</ul>{btn}</div>'
    sec='section alt' if alt else 'section'
    return f'<section class="{sec}"><div class="wrap"><div class="frow{" rev" if rev else ""}">{text}<div class="fvisual">{visual}</div></div></div></section>'

HEAT_MOCK="""<div class="mock"><div class="mockbar"><em></em><em></em><em></em><span class="url">yourstore.com</span></div>
<div class="mockbody hm"><div class="bar"></div>
<div class="ln l"></div><div class="ln m"></div><div class="ln s"></div>
<span class="cta"></span>
<div class="ln m" style="margin-top:26px;"></div><div class="ln l"></div><div class="ln s"></div>
<span class="blob" style="width:154px;height:154px;top:92px;left:26px;background:radial-gradient(circle,rgba(255,59,47,.92),rgba(255,179,0,.55) 52%,transparent 72%);"></span>
<span class="blob" style="width:98px;height:98px;top:150px;left:158px;background:radial-gradient(circle,rgba(255,80,40,.85),rgba(255,212,0,.5) 52%,transparent 72%);"></span>
<span class="blob" style="width:72px;height:72px;top:58px;left:64px;background:radial-gradient(circle,rgba(22,179,163,.7),transparent 70%);"></span>
<span class="blob" style="width:62px;height:62px;top:214px;left:54px;background:radial-gradient(circle,rgba(123,110,240,.5),transparent 72%);"></span></div></div>"""

DASH_MOCK="""<div class="mock"><div class="mockbar"><em></em><em></em><em></em><span class="url">Matomo · Behaviour</span></div>
<div class="mockbody"><div class="tiles">
<div class="tile"><span class="tl">Unique visitors</span><b>73k</b><i class="up">+5.2%</i></div>
<div class="tile"><span class="tl">Avg. time</span><b>2m15s</b><i class="up">+2.1%</i></div>
<div class="tile"><span class="tl">Bounce rate</span><b>16%</b><i class="down">-0.2%</i></div></div>
<svg class="chart" viewBox="0 0 320 150" preserveAspectRatio="none"><defs><linearGradient id="ga" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#16b3a3" stop-opacity=".22"/><stop offset="1" stop-color="#16b3a3" stop-opacity="0"/></linearGradient></defs>
<polygon fill="url(#ga)" points="0,108 40,80 80,94 120,52 160,68 200,32 240,50 280,24 320,40 320,150 0,150"/>
<polyline fill="none" stroke="#16b3a3" stroke-width="2.5" points="0,108 40,80 80,94 120,52 160,68 200,32 240,50 280,24 320,40"/></svg></div></div>"""

COMPLIANCE_MOCK="""<div class="mock"><div class="mockbar"><em></em><em></em><em></em><span class="url">Privacy &amp; compliance</span></div>
<div class="mockbody" style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;text-align:center;">
<div style="width:66px;height:66px;border-radius:18px;background:var(--teal-soft);display:flex;align-items:center;justify-content:center;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0f8a7e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/><path d="M9 12l2 2 4-4"/></svg></div>
<div style="display:flex;flex-wrap:wrap;gap:9px;justify-content:center;max-width:310px;"><span class="cbadge">GDPR</span><span class="cbadge">CCPA</span><span class="cbadge">HIPAA</span><span class="cbadge">CNIL approved</span><span class="cbadge">EU hosting</span><span class="cbadge">Consent-free</span></div>
</div></div>"""

STORE_MOCK="""<div class="mock"><div class="mockbar"><em></em><em></em><em></em><span class="url">yourstore.com/product</span></div>
<div class="mockbody" style="display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:center;">
<div style="height:160px;border-radius:12px;background:linear-gradient(135deg,#16b3a3,#15163a);display:flex;align-items:center;justify-content:center;color:#fff;font-size:34px;"><i class="ti ti-shirt"></i></div>
<div><div style="height:11px;width:75%;background:#edeff6;border-radius:6px;margin-bottom:11px;"></div><div style="height:11px;width:55%;background:#edeff6;border-radius:6px;margin-bottom:18px;"></div><div style="font-size:22px;font-weight:700;color:var(--navy);margin-bottom:16px;">$49.00</div><span style="display:inline-block;background:var(--navy);color:#fff;border-radius:9px;padding:11px 24px;font-size:13px;font-weight:600;">Add to cart</span></div>
</div></div>"""

OWNERSHIP_MOCK="""<div class="mock"><div class="mockbar"><em></em><em></em><em></em><span class="url">Where your data lives</span></div>
<div class="mockbody" style="display:flex;flex-direction:column;justify-content:center;gap:0;">
<div class="ownrow good"><div class="oic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01"/></svg></div><div><b>Matomo</b><span class="od">Your servers or EU-based cloud</span></div><span class="otag">You own 100%</span></div>
<div class="ownrow badrow"><div class="oic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01"/></svg></div><div><b>Google Analytics</b><span class="od">Google's servers, used for ads</span></div><span class="otag">Google owns it</span></div>
</div></div>"""

def testimonials(h2,items,sub=""):
    cards="".join(f'<div class="tm"><div class="stars">★★★★★</div><p class="q">"{q}"</p><div class="who"><span class="av">{ini}</span><div><b>{name}</b><span>{role}</span></div></div></div>' for q,name,role,ini in items)
    subhtml=f'<p>{sub}</p>' if sub else ''
    return f'<section class="section alt"><div class="wrap"><div class="sec-head"><h2>{h2}</h2>{subhtml}</div><div class="tmgrid">{cards}</div></div></section>'

def morelinks(h2,sub,items,alt=False):
    cards="".join(f'<a class="ml" href="#"><div class="mic"><i class="ti {ic}"></i></div><h3>{t}</h3><p>{d}</p><span class="go">Explore <i class="ti ti-arrow-right"></i></span></a>' for ic,t,d in items)
    sec='section alt' if alt else 'section'
    return f'<section class="{sec}"><div class="wrap"><div class="sec-head"><h2>{h2}</h2><p>{sub}</p></div><div class="mlgrid">{cards}</div></div></section>'

GA_TESTI=[
("We moved off Google Analytics for GDPR reasons and never looked back. Same depth of reporting, none of the legal risk, and the data is finally ours.","Marta L.","Head of Data, EU SaaS","ML"),
("GA4 sampling was quietly distorting our reports. With Matomo every number is real, and our DPO signed off without a fight.","James O.","Growth Lead, ecommerce","JO"),
("Switching was painless: we imported our history, ran both in parallel for a month, then dropped Google for good.","Sofia R.","Marketing Manager, media","SR")]
EC_TESTI=[
("Matomo's funnels showed exactly where checkout was leaking. We fixed two steps and recovered revenue in the first month.","Daniel K.","Ecommerce Director","DK"),
("Accurate, unsampled revenue data we actually own, and GDPR-ready, so we measure every visitor without a consent wall.","Aisha M.","Head of Growth, retail","AM"),
("Finally one tool for traffic, behaviour and sales, no more stitching Google Analytics to a separate heatmap tool.","Tom B.","Founder, DTC brand","TB")]
FEAT_TESTI=[
("Matomo's heatmaps showed our main CTA was below the fold on mobile. One fix lifted sign-ups by 18%, without sending a single byte to a third party.","Laura P.","Head of Growth, SaaS","LP"),
("Scroll maps told us exactly where readers dropped off. We moved our pricing block up and demo requests jumped.","Marco D.","CRO Manager, B2B","MD"),
("Finally heatmaps and analytics in one privacy-first tool, no more bolting a third-party recorder onto our stack.","Hana K.","Product Lead, fintech","HK")]
CMS_TESTI=[
("We added the Matomo plugin in minutes and finally own our WordPress analytics, no consent banner, no data shared with Google.","Julien R.","Webmaster, agency","JR"),
("Same insights as Google Analytics, right inside the WordPress dashboard, and our visitors' data never leaves our server.","Sara T.","Marketing Lead, publisher","ST"),
("Heatmaps, goals and WooCommerce sales in one plugin. It replaced three separate tools on our site.","Ben A.","Founder, WooCommerce store","BA")]
FEAT_LINKS=[
("ti-player-play","Session recordings","Replay real sessions to see the why behind the heatmap."),
("ti-arrows-split-2","A/B testing","Test changes and measure the impact on conversions."),
("ti-filter","Funnel analysis","Find exactly where visitors drop out of your funnels."),
("ti-tags","Tag Manager","Manage tags and triggers without touching code.")]
CMS_LINKS=[
("ti-shopping-bag","WooCommerce","Ecommerce analytics inside your WordPress store."),
("ti-brand-shopify","Shopify","Privacy-first analytics for your Shopify storefront."),
("ti-template","Drupal","Track any Drupal site with the Matomo module."),
("ti-puzzle","Joomla, Wix & more","A universal tag and integrations for every platform.")]
IND_LINKS=[
("ti-cloud","SaaS analytics","Track activation, retention and product usage, privately."),
("ti-heartbeat","Healthcare","HIPAA-ready analytics for patient-facing sites."),
("ti-building-bank","Finance","Compliant measurement for banks and fintech."),
("ti-building-community","Government","Data-sovereign analytics trusted by public bodies.")]

pages={}

# ============ 1. FEATURE LANDING, Heatmaps ============
pages['1-feature-landing-heatmaps.html']=shell(
"Website Heatmap Software, Clicks & Scrolls | Matomo",
"See where visitors click, scroll and drop off with Matomo's privacy-first, cookieless website heatmap software. 100% data ownership. Start free.",
hero("Behaviour analytics","Website heatmap software<br>that respects privacy",
"See where visitors click, move and scroll, and turn that behaviour into conversions, without sending a byte to third parties.",
"Start your free trial","Book a demo","No credit card · Cookieless · Trusted by 1M+ websites",ratings=True)
+ CLIENTS
+ '<section class="section"><div class="wrap"><div class="sec-head"><h2>Three ways to understand your visitors</h2><p>Click, scroll and movement maps reveal what traffic numbers never can.</p></div>'
+ '<div class="grid g3">'
+ '<div class="card"><div class="ic"><i class="ti ti-click"></i></div><h3>Click maps</h3><p>See which links and buttons earn clicks, and which non-clickable elements confuse visitors and waste attention.</p></div>'
+ '<div class="card"><div class="ic"><i class="ti ti-arrows-vertical"></i></div><h3>Scroll maps</h3><p>Know exactly how far visitors read, so your key message and CTAs never sit unseen below the fold.</p></div>'
+ '<div class="card"><div class="ic"><i class="ti ti-pointer"></i></div><h3>Move maps</h3><p>Follow mouse movement as a proxy for attention, and find the zones that genuinely engage people.</p></div>'
+ '</div></div></section>'
+ frow("Behaviour, visualised","See how Matomo maps every click, scroll and move",
"Matomo turns thousands of visits into click, scroll and movement maps, so you see what people actually do, not just how many showed up. And unlike Hotjar or Crazy Egg, every map is built from cookieless, first-party data you fully own.",
["Click maps: which buttons and links earn attention, and which dead zones confuse.",
"Scroll maps: how far visitors really read, so key messages are never missed.",
"Move maps: mouse movement as a proxy for where attention goes.",
"100% data ownership and cookieless, unlike Hotjar or Crazy Egg."],
"Start your free trial", HEAT_MOCK, rev=True, alt=True, note=True)
+ frow("Grow conversions","Turn behaviour into conversions",
"Used alongside funnels and A/B testing, heatmaps replace opinions with evidence, so every design decision is backed by what real visitors do, and every CRO experiment targets the friction that actually costs you revenue.",
["Pinpoint why visitors abandon a page or checkout step before converting.",
"Check whether key calls-to-action are actually seen, or buried below the fold.",
'Find distractions and "false bottoms" that stop people reaching your offer.',
"Validate redesigns with before/after evidence, not guesswork.",
"Prioritise CRO experiments based on where real attention and friction sit."],
"Start your free trial", DASH_MOCK, rev=False, alt=False)
+ '<section class="section dark"><div class="wrap" style="max-width:640px;text-align:center;"><div style="width:52px;height:52px;border-radius:14px;background:var(--navy2);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;"><i class="ti ti-lock" style="color:var(--teal-bright);font-size:26px;"></i></div>'
+ '<h2>Heatmaps that don\'t leak your data</h2>'
+ '<p style="margin:14px 0 24px;">Unlike Hotjar or Crazy Egg, Matomo keeps 100% of your behaviour data on your own servers or EU-based cloud. Cookieless tracking, IP anonymisation and a built-in GDPR Manager mean you can often run heatmaps without a consent banner, fully compliant with GDPR, CCPA and HIPAA.</p>'
+ '<div><span class="pill">100% data ownership</span><span class="pill">Cookieless</span><span class="pill">GDPR · CCPA · HIPAA</span><span class="pill">Self-hosted or EU cloud</span></div></div></section>'
+ '<section class="section"><div class="wrap"><div class="sec-head"><h2>Up and running in minutes</h2></div><div class="steps">'
+ '<div class="step"><span class="n">1</span><div><h3>Add the tag or plugin</h3><p>One snippet, or a one-click install on WordPress and Matomo Cloud, no developer required.</p></div></div>'
+ '<div class="step"><span class="n">2</span><div><h3>Choose your pages</h3><p>Pick which URLs to record and set a sample size. Heatmaps build automatically as visits come in.</p></div></div>'
+ '<div class="step"><span class="n">3</span><div><h3>Act on the insight</h3><p>Read the maps, segment by device or source, and feed findings straight into A/B tests and funnels.</p></div></div>'
+ '</div></div></section>'
+ morelinks("Explore more Matomo features","Heatmaps work even better alongside the rest of the privacy-first behaviour suite.", FEAT_LINKS)
+ testimonials("What teams see with Matomo heatmaps", FEAT_TESTI, "Real wins from teams using behaviour analytics that respect privacy.")
+ learnmore([
("ti-flame","Guide","What is a website heatmap?","A clear, illustrated guide to click, scroll and move maps, and how to read them.","Read the guide"),
("ti-arrow-down-circle","Blog","How to reduce bounce rate","Practical fixes to keep visitors engaged, backed by heatmap and scroll data.","Read the blog"),
("ti-versus","Comparison","Matomo vs Google Analytics","See how Matomo compares to Google Analytics on privacy, accuracy and cost.","Compare tools"),
])
+ faq([
("What is a website heatmap?","A website heatmap is a visual report of how visitors interact with a page: warm colours show where clicks, scrolls and attention concentrate, cool colours show what gets ignored. Matomo builds them from cookieless, first-party data, across desktop, tablet and mobile."),
("Are Matomo heatmaps GDPR compliant?","Yes. Matomo records heatmaps with first-party, cookieless tracking and IP anonymisation, and you keep 100% data ownership. In many jurisdictions this lets you run heatmaps without a consent banner."),
("How is Matomo different from Hotjar or Crazy Egg?","Hotjar and Crazy Egg send your visitors' behaviour to their own servers. Matomo lets you self-host or use EU-based cloud, so the data never leaves your control, and heatmaps sit in the same platform as your web analytics."),
("Can I use heatmaps without a cookie consent banner?","In many cases yes. Matomo's cookieless configuration and CNIL-recognised privacy controls allow consent-free tracking in several jurisdictions. Always confirm with your DPO for your specific case."),
("Do heatmaps slow down my website?","No. Matomo loads asynchronously and samples sessions, so there is no measurable impact on page-load performance."),
])
+ callout("See what your visitors really do","Start mapping clicks and scrolls today, free for 21 days, no credit card.","Start your free trial"))

# ============ 2. VS PAGE, Matomo vs Google Analytics ============
CK_YES='<span class="ck yes"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13l4 4L19 7"/></svg></span>'
CK_NO='<span class="ck no"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="#8a8ca6" stroke-width="3.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></span>'
def cmpcell(v): return CK_YES if v=="yes" else ('<span class="pp">Partial</span>' if v=="part" else CK_NO)
def cmptable_grouped(comp,groups):
    rows=""
    for cat,items in groups:
        rows+=f'<tr class="cat"><td class="col-crit">{cat}</td><td class="col-mat"></td><td class="col-comp"></td></tr>'
        rows+="".join(f'<tr><td class="col-crit">{c}</td><td class="col-mat">{cmpcell(m)}</td><td class="col-comp">{cmpcell(g)}</td></tr>' for c,m,g in items)
    return ('<div class="cmp2-wrap"><table class="cmp2"><thead><tr>'
    '<th class="col-crit">What matters</th>'
    '<th class="col-mat"><span class="mat-logo">Matomo</span><span class="rec">Recommended</span></th>'
    f'<th class="col-comp">{comp}</th></tr></thead><tbody>{rows}</tbody></table></div>')
GA_GROUPS=[
("Privacy & data ownership",[("100% data ownership","yes","no"),("Cookieless / consent-free tracking","yes","no"),("No data sampling","yes","no"),("GDPR Manager & privacy controls","yes","part"),("Raw data access (SQL / API)","yes","part")]),
("Hosting",[("Cloud hosting","yes","yes"),("On-premise self-hosting","yes","no")]),
("Behaviour analytics",[("Heatmaps","yes","no"),("Session recordings","yes","no"),("A/B testing","yes","no"),("Form analytics","yes","no"),("Funnels & goals","yes","part")]),
("Reporting & data",[("Unsampled reports","yes","no"),("Custom dimensions & segments","yes","yes"),("Ecommerce reporting","yes","yes"),("Roll-up reporting","yes","no"),("No hit / volume limits","yes","no")]),
("Integrations",[("Google Ads integration","part","yes"),("Search Console integration","yes","yes"),("Tag manager","yes","yes")]),
("Pricing",[("Free / open-source option","yes","yes")])]
cmp_table=cmptable_grouped("Google Analytics",GA_GROUPS)
pages['2-vs-page-google-analytics.html']=shell(
"Matomo vs Google Analytics: Honest 2026 Comparison",
"Matomo vs Google Analytics compared: privacy, data ownership, accuracy, pricing and features. See why teams switch to the privacy-first alternative.",
hero("Comparison","Matomo vs Google Analytics",
"Choosing the right Google Analytics alternative is critical. See exactly how the two differ on privacy, data ownership, accuracy and cost, no spin.",
"Get started for free","Book a demo","No credit card required · Import your historical data")
+ '<section class="section" style="padding-bottom:0;"><div class="wrap" style="max-width:760px;"><div class="callout" style="background:var(--teal-soft);text-align:left;padding:34px 36px;"><h3 style="font-size:20px;margin-bottom:10px;">The verdict in one line</h3><p style="color:#3f6b62;max-width:none;margin:0;font-size:17px;">Choose <b>Matomo</b> for 100% data ownership, unsampled data and GDPR peace of mind. Choose <b>Google Analytics</b> if you live inside Google Ads and don\'t need to own your data.</p></div></div></section>'
+ '<section class="section"><div class="wrap" style="max-width:880px;"><div class="sec-head"><h2>Feature-by-feature comparison'+A_CMP+'</h2><p>The criteria that matter most, grouped by theme, with an honest read on where each tool wins.</p></div>'+cmp_table+'<p style="text-align:center;font-size:14px;color:var(--muted2);margin-top:14px;">And more in the full comparison.</p><div style="text-align:center;margin-top:28px;"><a class="btn btn-navy">Start your free trial</a></div></div></section>'
+ '<section class="section alt"><div class="wrap"><div class="stats">'
+ '<div class="stat"><div class="big">No limits</div><p>on Matomo data. Google Analytics stops at 10M hits; GA360 costs ≈ $130k/yr</p></div>'
+ '<div class="stat"><div class="big">100%</div><p>accurate, unsampled data. GA4 samples large reports</p></div>'
+ '<div class="stat"><div class="big">CNIL</div><p>approved for consent-free tracking in France</p></div>'
+ '</div></div></section>'
+ frow("Privacy & compliance","Compliant by design, not by project",
"Google Analytics has been ruled illegal under GDPR in France and Austria for transferring EU data to the US. Matomo is trusted on privacy by the European Commission, the non-profit noyb, and France's CNIL, which cleared it for consent-free tracking.",
["EU-hosted data, with IP anonymisation and first-party cookies.",
"CNIL-approved for tracking without a consent banner in France.",
"Compliant with GDPR, CCPA and HIPAA out of the box."],
"Start your free trial", COMPLIANCE_MOCK, rev=True, alt=False, note=True)
+ frow("Data ownership","Your data stays 100% yours",
"With Google Analytics, your data lives on Google's servers and feeds its advertising products. With Matomo, you own every data point, self-hosted or on EU-based cloud, and can export all of it whenever you want.",
["Self-host on your own infrastructure, or use EU-based Matomo Cloud.",
"Export every raw data point via SQL or API, with no lock-in.",
"Visitor data is never sold, shared or mined for ads."],
"Book a demo", OWNERSHIP_MOCK, rev=False, alt=True)
+ frow("Data accuracy","Unsampled data you can actually trust",
"GA4 starts sampling once a report passes roughly 10 million rows, adding guesswork to the numbers your decisions rest on. Matomo processes 100% of your traffic, with no sampling and no hit limits.",
["No data sampling, ever. The report you read is the reality.",
"No hit limits, and no surprise GA360 bill at scale.",
"Raw, unaggregated data you can audit line by line."],
"Start your free trial", DASH_MOCK, rev=True, alt=False)
+ testimonials("Why they chose Matomo over Google Analytics", GA_TESTI, "Real reasons teams leave Google Analytics, in their own words.")
+ '<section class="section"><div class="wrap" style="max-width:760px;"><div style="background:#fff;border:1px solid var(--line);border-left:3px solid #d4843a;border-radius:12px;padding:22px 24px;margin:0 0 22px;"><h3 style="font-size:17px;margin-bottom:6px;color:var(--navy);">Where Google Analytics wins</h3><p style="margin:0;font-size:16px;color:var(--muted);">Native Google Ads and Marketing Platform integration, plus a huge ecosystem of tutorials. If your stack is 100% Google and data ownership is not a concern, GA can fit. On privacy, ownership, accuracy and behaviour analytics, Matomo leads.</p></div>'
+ '<div class="related"><strong>Keep comparing:</strong>'+A_KEEPCMP+' <a>Matomo vs Piwik PRO</a> · <a>Matomo vs Plausible</a> · <a>Best Google Analytics alternatives</a> · <a>How to migrate from GA to Matomo</a></div></div></section>'
+ learnmore([
("ti-arrows-exchange","Guide","How to migrate from Google Analytics to Matomo","A step-by-step migration plan, import your history and run both in parallel.","Read the guide"),
("ti-shield-x","Blog","Is Google Analytics GDPR compliant?","What the EU rulings mean for your site, and how to stay on the right side of the law.","Read the blog"),
("ti-list-search","Comparison","Best Google Analytics alternatives","The privacy-first analytics tools worth considering in 2026, compared.","See the list"),
])
+ faq([
("Is Google Analytics GDPR compliant?","Google Analytics has been found non-compliant with GDPR by several EU regulators due to US data transfers. Matomo is designed to be GDPR compliant out of the box, with EU hosting and consent-free options."),
("Can I migrate my GA4 or Universal Analytics data to Matomo?","Yes. Matomo can import historical Universal Analytics data and you can run both in parallel during a switch, so you lose no history."),
("Is Matomo free?","Matomo On-Premise is free and open source. Matomo Cloud is a paid hosted plan with a free trial. Both give you 100% data ownership."),
("Does Matomo sample data like GA4?","No. Matomo processes 100% of your traffic with no sampling and no hit limits."),
])
+ callout("Own your analytics. Drop the data limits.","Try Matomo free for 21 days, or self-host it for free, your data, your servers.","Get started for free"))

# ============ 4. CMS LANDING, WordPress Analytics ============
pages['4-cms-landing-wordpress.html']=shell(
"WordPress Analytics Plugin, Easy Setup | Matomo",
"Add privacy-first analytics to WordPress in minutes with the official Matomo plugin. Heatmaps, goals and GDPR-ready tracking, no coding, no consent banner.",
hero("WordPress analytics","Privacy-first analytics<br>for WordPress",
"Install the official Matomo plugin and get powerful, GDPR-ready analytics right inside your WordPress dashboard, no code, no consent banner, no data sharing.",
"Add to WordPress","Start free trial","One-click install · 1M+ websites · Cookieless",ratings=True)
+ CLIENTS
+ '<section class="section"><div class="wrap"><div class="sec-head"><h2>Set up in 3 steps, no developer</h2></div><div class="steps">'
+ '<div class="step"><span class="n">1</span><div><h3>Install the plugin</h3><p>Search "Matomo" in your WordPress plugins, install and activate, like any other plugin.</p></div></div>'
+ '<div class="step"><span class="n">2</span><div><h3>Tracking starts automatically</h3><p>No tag to paste, no theme edits. Matomo begins collecting data the moment it\'s active.</p></div></div>'
+ '<div class="step"><span class="n">3</span><div><h3>See reports in your dashboard</h3><p>Traffic, goals, heatmaps and more, right inside WordPress, or in the full Matomo interface.</p></div></div>'
+ '</div></div></section>'
+ shot("Matomo reports inside the WordPress admin")
+ '<section class="section alt"><div class="wrap"><div class="sec-head"><h2>Everything WordPress analytics should have</h2></div><div class="grid g3">'
+ '<div class="card"><div class="ic"><i class="ti ti-shield-lock"></i></div><h3>No consent banner</h3><p>Cookieless, GDPR-ready tracking that works without a cookie pop-up in many countries.</p></div>'
+ '<div class="card"><div class="ic"><i class="ti ti-database"></i></div><h3>Your data, on your host</h3><p>Store analytics in your own WordPress database, nothing shared with Big Tech.</p></div>'
+ '<div class="card"><div class="ic"><i class="ti ti-click"></i></div><h3>Heatmaps & goals built in</h3><p>Go beyond pageviews with heatmaps, goals and ecommerce tracking for WooCommerce.</p></div>'
+ '</div></div></section>'
+ morelinks("Other integrations","Matomo plugs into every major CMS and platform, not just WordPress.", CMS_LINKS)
+ testimonials("What WordPress teams say", CMS_TESTI, "From agencies to publishers, why WordPress sites switch to Matomo.")
+ '<section class="section"><div class="wrap prose"><h2>Why WordPress sites choose Matomo</h2>'
+ '<p>WordPress powers a huge share of the web, and most sites bolt on Google Analytics by default, handing visitor data to a third party and triggering a consent banner. Matomo\'s official plugin keeps analytics inside your own WordPress install, so you own the data and stay compliant without the friction.</p>'
+ '<p>Because it\'s the same Matomo platform, you also get heatmaps, session recordings, goals, funnels and WooCommerce ecommerce reporting, no second tool, no extra data processor to vet.</p>'
+ '<div class="related"><strong>Related:</strong> <a>WooCommerce analytics</a> · <a>Cookieless tracking</a> · <a>GDPR-compliant analytics</a> · <a>Matomo vs Google Analytics</a></div></div></section>'
+ learnmore([
("ti-plug","Guide","How to add analytics to WordPress","Step-by-step: install, configure and start tracking without touching code.","Read the guide"),
("ti-shield-check","Blog","WordPress GDPR compliance","What WordPress site owners must know about cookies, consent and visitor data.","Read the blog"),
("ti-shopping-cart","Use case","WooCommerce analytics","Track sales, products and cart abandonment inside your WordPress store.","Explore"),
])
+ faq([
("Is the Matomo WordPress plugin free?","Yes. The Matomo for WordPress plugin is free and open source. You can also connect a WordPress site to Matomo Cloud."),
("Do I need a consent banner with Matomo on WordPress?","In many jurisdictions, no. Matomo\'s cookieless configuration allows consent-free tracking, always confirm with your DPO."),
("Does it work with WooCommerce?","Yes. Matomo includes ecommerce reporting that tracks WooCommerce sales, products and conversion rates."),
("Will it slow down my WordPress site?","No. Matomo tracking is lightweight and loads asynchronously, with no measurable impact on page speed."),
])
+ callout("Add privacy-first analytics to WordPress","Install the official plugin and start tracking in minutes, free.","Add to WordPress"))

# ============ 5. USE CASE LANDING, Ecommerce Analytics ============
pages['5-use-case-ecommerce.html']=shell(
"Ecommerce Analytics, Track Every Sale | Matomo",
"Matomo ecommerce analytics shows you revenue, top products, cart abandonment and the full customer journey, with 100% data ownership and no data limits.",
hero("Use case · Ecommerce","Ecommerce analytics<br>that grows revenue",
"Track every sale, product and abandoned cart, and see the full journey from first visit to checkout, with data you fully own.",
"Start your free trial","Book a demo","No credit card · GDPR-ready · For Shopify, WooCommerce & more",ratings=True)
+ CLIENTS
+ frow("The challenge","Traffic is easy, revenue insight is hard",
"Most ecommerce teams can see how many people visit, but not why carts are abandoned, which products convert, or where revenue leaks in the funnel. And the default tools sample data and ship it to third parties, which is a problem when traffic equals revenue and customers expect privacy.",
[], "", STORE_MOCK, rev=False, alt=False)
+ '<section class="section alt"><div class="wrap"><div class="sec-head"><h2>How Matomo helps you sell more</h2><p>Every report mapped to a revenue question.</p></div><div class="grid g3">'
+ '<div class="card"><div class="ic"><i class="ti ti-shopping-cart"></i></div><h3>Revenue & product reports</h3><p>See sales, revenue, average order value and best/worst performing products in real time.</p></div>'
+ '<div class="card"><div class="ic"><i class="ti ti-filter"></i></div><h3>Cart & checkout funnels</h3><p>Find exactly which step loses buyers, then fix it with heatmaps and session recordings.</p></div>'
+ '<div class="card"><div class="ic"><i class="ti ti-route"></i></div><h3>Full customer journey</h3><p>Attribute revenue to the right channels and campaigns across the whole path to purchase.</p></div>'
+ '</div></div></section>'
+ shot("Ecommerce overview, revenue, conversion rate, top products")
+ '<section class="section"><div class="wrap prose"><h2>Built for regulated, privacy-conscious commerce</h2>'
+ '<p>Matomo gives you accurate, unsampled ecommerce data with 100% ownership, hosted on your servers or EU-based cloud. Cookieless tracking keeps you compliant with GDPR and reduces consent friction, so you measure more visitors and lose fewer data points than consent-gated tools.</p>'
+ '<p>It works with Shopify, WooCommerce, Magento, PrestaShop and custom stores, and connects ecommerce data to heatmaps, funnels, A/B testing and attribution, one platform for the whole conversion picture.</p>'
+ '<div class="related"><strong>Related:</strong> <a>Conversion funnels</a> · <a>WooCommerce analytics</a> · <a>How to reduce cart abandonment</a> · <a>Ecommerce KPIs that matter</a></div></div></section>'
+ testimonials("What ecommerce teams say", EC_TESTI, "Real results from stores that switched to privacy-first, fully-owned analytics.")
+ morelinks("Analytics for every industry","Ecommerce is just the start. Matomo fits regulated and privacy-conscious sectors.", IND_LINKS)
+ learnmore([
("ti-shopping-cart-off","Blog","How to reduce cart abandonment","Find where buyers drop off in checkout and the fixes that recover revenue.","Read the blog"),
("ti-chart-bar","Guide","Ecommerce KPIs that matter","The metrics that actually move revenue, and how to track them accurately.","Read the guide"),
("ti-trending-up","Blog","Ecommerce conversion optimization","A practical CRO playbook for online stores, from funnels to A/B testing.","Read the blog"),
])
+ faq([
("Does Matomo work with Shopify and WooCommerce?","Yes. Matomo integrates with Shopify, WooCommerce, Magento, PrestaShop and custom stores to track sales, products and revenue."),
("Is ecommerce data sampled?","No. Matomo processes 100% of your ecommerce data with no sampling, so revenue figures are accurate."),
("Can I track cart abandonment?","Yes. Ecommerce funnels show exactly where buyers drop off, and heatmaps/recordings help you understand why."),
("Do I own my ecommerce data?","Yes. You keep 100% data ownership, self-hosted or on EU-based Matomo Cloud."),
])
+ callout("Turn store traffic into revenue you understand","Start your free 21-day trial, accurate ecommerce analytics you own.","Start your free trial"))

# ============ 6. BLOG PILLAR, What is bounce rate ============
pages['6-blog-pillar-bounce-rate.html']=shell(
"What Is Bounce Rate? A Good Average Explained | Matomo",
"What is bounce rate, what counts as a good bounce rate, and how do you reduce it? A clear guide with formulas, benchmarks and practical fixes.",
'<section class="hero" style="padding:70px 0 34px;text-align:left;"><div class="wrap"><div style="max-width:760px;"><span class="eyebrow">Web analytics · Guide</span><h1 style="font-size:40px;margin:20px 0 16px;">What is bounce rate? Definition, benchmarks &amp; how to improve it</h1><p class="lead" style="margin:0;max-width:none;">Bounce rate is one of the most quoted, and most misunderstood, web metrics. Here\'s what it really measures, what a good rate looks like, and how to lower it.</p><div class="byline"><span class="avatar">SM</span><div class="bmeta"><b>Sophie Martin</b><span>Web Analytics Lead at Matomo · Updated June 2026 · 9 min read</span></div></div></div></div></section>'
+ '<section class="section" style="padding-top:40px;"><div class="wrap"><div class="article"><div class="acontent">'
+ '<div class="inbrief"><h3><i class="ti ti-bolt"></i> TL;DR'+A_INBRIEF+'</h3><ul>'
+ '<li>Bounce rate is the share of visits where someone views a single page and leaves with no further interaction.</li>'
+ '<li>The formula is simple: single-page visits ÷ total visits × 100.</li>'
+ '<li>A "good" rate depends on page type, 65-90% is normal for content, 20-45% for ecommerce and SaaS.</li>'
+ '<li>A high bounce rate isn\'t always bad: read it alongside time on page, scroll depth and conversions.</li>'
+ '<li>Lower it by matching search intent, improving page speed, and using heatmaps to fix what visitors ignore.</li>'
+ '</ul></div>'
+ '<div class="toc"><strong>In this guide</strong><a href="#def">What is bounce rate?</a><a href="#calc">How to calculate bounce rate</a><a href="#good">What is a good bounce rate?</a><a href="#why">Why your bounce rate matters</a><a href="#reduce">How to reduce bounce rate</a></div>'
+ '<div class="prose">'
+ '<p id="def"><b>Bounce rate is the percentage of visits in which a person views a single page and then leaves without any further interaction.</b> If 100 people land on a page and 60 leave without clicking, scrolling-tracked events, or visiting another page, the bounce rate is 60%.</p>'
+ '<h2 id="calc">How to calculate bounce rate</h2><p>The formula is simple:</p>'
+ '<div style="background:var(--bg2);border-radius:12px;padding:20px 24px;margin:0 0 22px;font-size:17px;color:var(--navy);"><b>Bounce rate = single-page visits ÷ total visits × 100</b></div>'
+ '<p>So 300 bounces out of 1,000 visits is a 30% bounce rate. In Matomo you don\'t calculate it by hand, it\'s shown per page, per channel and per segment automatically, and you can define what counts as engagement.</p>'
+ '<h2 id="good">What is a good bounce rate?</h2><p>There\'s no universal number, context is everything. As rough benchmarks:</p>'
+ '<ul><li><b>Content / blog pages:</b> 65-90% is normal, people read and leave satisfied.</li>'
+ '<li><b>Landing pages:</b> 60-90%, though high rates can signal a mismatch with the ad or query.</li>'
+ '<li><b>Ecommerce / SaaS:</b> 20-45% is healthy, visitors are expected to browse and convert.</li></ul>'
+ '<p>A high bounce rate isn\'t always bad. If someone finds your phone number and leaves happy, that\'s a success the metric counts as a bounce. Always read it alongside time on page, scroll depth and conversions.</p>'
+ '<h2 id="why">Why your bounce rate matters</h2><p>Bounce rate is an early signal of relevance and experience. A sudden spike often points to a broken page, slow load time, a misleading title, or traffic from the wrong keywords. Segmented by device or source, it tells you <em>where</em> the experience breaks down.</p>'
+ '<h2 id="reduce">How to reduce bounce rate</h2>'
+ '<ul><li>Match page content to the search intent and the ad that brought the visitor.</li>'
+ '<li>Improve page-load speed, slow pages bounce hardest, especially on mobile.</li>'
+ '<li>Use heatmaps and scroll maps to see where attention drops, then move key content up.</li>'
+ '<li>Add clear next steps and internal links so there\'s an obvious action to take.</li>'
+ '<li>Test changes with A/B testing and watch the effect on bounce and conversions together.</li></ul>'
+ '<div style="background:var(--teal-soft);border-radius:14px;padding:24px 26px;margin:30px 0;"><p style="margin:0;font-size:16px;color:#2b4d47;"><b>Measure bounce rate the privacy-first way.</b> Matomo shows accurate, unsampled bounce rate by page, channel and segment, and pairs it with heatmaps so you can see <em>why</em> people leave. <a>Start a free trial →</a></p></div>'
+ '<div class="related"><strong>Related reading:</strong> <a>What is a good conversion rate?</a> · <a>How to reduce cart abandonment</a> · <a>Website heatmap software</a> · <a>Exit rate vs bounce rate</a></div>'
+ '</div></div>'
+ '<aside class="asidebar">'
+ '<div class="sidecta dark"><div class="st">Start free</div><h4>See your real bounce rate'+A_SIDECTA+'</h4><p>Accurate, unsampled analytics with 100% data ownership, no credit card needed.</p><a class="btn btn-teal">Start your free trial</a></div>'
+ '<div class="sidecta"><div class="st">Free playbook</div><h4>The privacy-first analytics playbook</h4><p>Join 50,000+ marketers and get one actionable, privacy-first analytics email a month.</p><div class="sideform"><input type="email" placeholder="you@company.com"><a class="btn btn-navy">Get the playbook</a></div></div>'
+ '</aside>'
+ '</div></div></section>'
+ '<section class="section" style="padding-top:0;"><div class="wrap"><div class="authorbox"><span class="avatar">SM</span><div class="ainfo"><h4>Sophie Martin'+A_AUTHOR+'</h4><div class="role">Web Analytics Lead at Matomo</div><p>Sophie helps privacy-conscious teams turn raw analytics into decisions that grow conversions. With 10+ years in web analytics and CRO, she writes about measuring what matters, without compromising user privacy.</p><div class="social"><a aria-label="LinkedIn"><i class="ti ti-brand-linkedin"></i></a><a aria-label="X"><i class="ti ti-brand-x"></i></a><a aria-label="Mastodon"><i class="ti ti-brand-mastodon"></i></a></div></div></div></div></section>'
+ learnmore([
("ti-target","Guide","What is a good conversion rate?","Benchmarks by industry and how to lift yours, with accurate, unsampled data.","Read the guide"),
("ti-shopping-cart-off","Blog","How to reduce cart abandonment","Find where buyers drop off in checkout and the fixes that recover revenue.","Read the blog"),
("ti-flame","Feature","Website heatmap software","See exactly where attention drops with click and scroll maps, the why behind bounce.","Explore heatmaps"),
])
+ callout("Stop guessing why visitors leave","See accurate bounce rate plus the heatmaps behind it, free for 21 days.","Start your free trial"))

# ============ 7. BLOG INDEX / LISTING ============
A_BLOGCATS=anno("Each category maps to a <b>topic cluster (semantic cocoon)</b> and its pillar page. Category pages become mini-hubs that capture a generic keyword, spread internal links and build topical authority. One primary category per article keeps the signal clean.","Blog categories &middot; topic clusters")
BLOG_CATS=["All","Privacy & compliance","Web analytics","Conversion optimization","Behavioral & product","Tracking & implementation","Marketing & growth","Google Analytics & switching","Product news"]
BLOG_FEAT=("Google Analytics & switching","Is Google Analytics GDPR compliant? What the 2026 rulings mean for you","EU regulators have repeatedly ruled Google Analytics non-compliant. Here is what that means for your website, and the privacy-first way to keep measuring without the legal risk.","Sophie Martin","SM","8 min read")
BLOG_POSTS=[
("Conversion optimization","What is a website heatmap? A complete guide","Click, scroll and move maps explained, and how to read them to lift conversions.","Sophie Martin","SM","7 min read",0),
("Privacy & compliance","GDPR-compliant analytics: the practical checklist","Everything you need to measure visitors without breaking GDPR, step by step.","Marc Hugo","MH","9 min read",1),
("Web analytics","What is bounce rate? Benchmarks and how to improve it","What it really measures, what counts as a good rate, and the fixes that work.","Sophie Martin","SM","9 min read",2),
("Google Analytics & switching","How to migrate from Google Analytics to Matomo","A painless migration plan: import your history, run in parallel, then switch.","Lea Bonnet","LB","6 min read",1),
("Behavioral & product","Customer journey analytics, explained with examples","Map the full path to conversion across channels, campaigns and pages.","Sophie Martin","SM","8 min read",2),
("Tracking & implementation","Server-side vs client-side tracking: what to know","The trade-offs, and when each makes sense for accuracy and privacy.","Marc Hugo","MH","7 min read",0),
("Privacy & compliance","Cookieless tracking: measure without consent banners","How first-party, cookieless analytics keeps you compliant and accurate.","Lea Bonnet","LB","6 min read",1),
("Marketing & growth","Ecommerce analytics: track every sale and cart","Revenue, products, funnels and attribution, with data you fully own.","Sophie Martin","SM","8 min read",2),
("Conversion optimization","A/B testing for conversion: a starter playbook","Run experiments that move revenue, backed by heatmaps and funnels.","Marc Hugo","MH","7 min read",0)]
def post_card(p):
    cat,title,excerpt,author,ini,read,g=p
    return f'<a class="post" href="6-blog-pillar-bounce-rate.html"><div class="img" style="background:{GRADS[g]};"><i class="ti ti-article"></i></div><div class="pbody"><span class="ptag">{cat}</span><h3>{title}</h3><p>{excerpt}</p><div class="pmeta"><span class="av">{ini}</span><div><b>{author}</b> · {read}</div></div></div></a>'
fcat,ftitle,fx,fauth,fini,fread=BLOG_FEAT
pills="".join(f'<a class="{"active" if c=="All" else ""}">{c}</a>' for c in BLOG_CATS)
pages['7-blog-index.html']=shell(
"Blog, Privacy-First Analytics Insights | Matomo",
"Guides, comparisons and how-tos on privacy-first web analytics, conversion optimisation and switching from Google Analytics. The Matomo blog.",
'<section class="hero" style="padding:74px 0 46px;"><div class="wrap"><span class="eyebrow">The Matomo blog</span><h1 style="max-width:680px;">Privacy-first analytics, explained</h1><p class="lead" style="max-width:560px;">Guides, comparisons and how-tos to help you measure what matters, grow conversions and own your data.</p></div></section>'
+ f'<section class="section" style="padding-top:30px;"><div class="wrap"><div class="bcat">{pills}</div>'
+ f'<div style="text-align:center;margin:-34px auto 24px;font-size:13px;color:var(--muted2);">Browse by topic{A_BLOGCATS}</div>'
+ f'<div class="feat"><div class="img" style="background:{GRADS[0]};"><i class="ti ti-shield-x"></i></div><div class="fbody"><span class="ftag">Featured · {fcat}</span><h2>{ftitle}</h2><p class="fx">{fx}</p><div class="pmeta"><span class="av">{fini}</span><div><b>{fauth}</b> · {fread}</div></div></div></div>'
+ f'<div class="postgrid">{"".join(post_card(p) for p in BLOG_POSTS)}</div>'
+ '<div class="pager"><a class="nav">‹ Prev</a><a class="active">1</a><a>2</a><a>3</a><span class="dots">…</span><a>7</a><a class="nav">Next ›</a></div>'
+ '</div></section>'
+ '<section class="section alt"><div class="wrap"><div class="callout"><h2>Get the privacy-first analytics playbook</h2><p>One actionable, privacy-first analytics email a month. Join 50,000+ marketers.</p><div class="sideform" style="flex-direction:row;max-width:400px;margin:0 auto;"><input type="email" placeholder="you@company.com"><a class="btn btn-navy">Subscribe</a></div></div></div></section>')

# ============ 8. COMPARE HUB ============
A_CMPHUB=anno("This hub links every <b>'Matomo vs ...' page</b> into one place. It captures broad comparison intent, meshes the whole comparison cluster for internal linking, and gives buyers one entry point to every decision they are weighing.","Comparison hub &middot; internal linking")
COMPARE_GROUPS=[
("Web analytics",[
("Google Analytics","Privacy, data ownership and accuracy vs the market default.","2-vs-page-google-analytics.html"),
("Adobe Analytics","Enterprise-grade analytics without the enterprise price or lock-in.","#")]),
("Privacy-first analytics",[
("Piwik PRO","Two Piwik descendants compared on features, model and openness.","#"),
("Plausible","Privacy-first like Plausible, with heatmaps, funnels and ecommerce built in.","#"),
("Fathom","Simple and private, plus the depth Fathom leaves out.","#")]),
("Product analytics",[
("Amplitude","Product and behaviour analytics with full data ownership.","#"),
("Mixpanel","Funnels and retention without sending data to a third party.","#"),
("Heap","Autocapture-style insight, self-hostable and GDPR-ready.","#")]),
("Behaviour & heatmaps",[
("Hotjar","Heatmaps and recordings plus full web analytics, data fully owned.","#"),
("Microsoft Clarity","Behaviour insight that is not fuelling an ad business.","#"),
("Crazy Egg","Click and scroll maps without third-party data storage.","#"),
("Mouseflow","Recordings and heatmaps in one privacy-first platform.","#")])]
def comparehub(groups):
    out=""
    for i,(cat,items) in enumerate(groups):
        cards="".join(f'<a class="cmpc" href="{href}"><div class="vs">Matomo <span>vs</span> {name}</div><p>{desc}</p><span class="go">See comparison <i class="ti ti-arrow-right"></i></span></a>' for name,desc,href in items)
        out+=f'<div class="cmpcat{" first" if i==0 else ""}">{cat}</div><div class="cmpgrid">{cards}</div>'
    return out
pages['8-compare-hub.html']=shell(
"Compare Matomo, Honest Analytics Comparisons | Matomo",
"See how Matomo compares to Google Analytics, Adobe, Piwik PRO, Plausible, Amplitude, Hotjar and more, on privacy, data ownership and depth.",
'<section class="hero" style="padding:74px 0 50px;"><div class="wrap"><span class="eyebrow">Compare</span><h1 style="max-width:700px;">See how Matomo compares</h1><p class="lead" style="max-width:580px;">Honest, detailed comparisons against every major analytics, product and behaviour tool, on privacy, data ownership and depth.</p></div></section>'
+ f'<section class="section" style="padding-top:18px;"><div class="wrap" style="max-width:980px;"><div style="font-size:13px;color:var(--muted2);margin-bottom:6px;">All comparisons{A_CMPHUB}</div>'
+ comparehub(COMPARE_GROUPS)
+ '</div></section>'
+ callout("Not sure which tool is right?","Start a free 21-day trial and see Matomo on your own data, no credit card needed.","Start your free trial"))

# ============ 9. FEATURES HUB ============
A_FHUB=anno("This hub centralises every feature and links to each feature landing page. It captures broad 'analytics features' intent, gives users one fast entry point, and meshes the entire product cluster for internal linking.","Features hub &middot; internal linking")
FEATURE_GROUPS=[
("measure","Measure & report",[
("ti-chart-line","Web analytics","All your traffic, visits and engagement in one place.","#"),
("ti-report","Custom reports","Build the exact reports your team needs, no SQL required.","#"),
("ti-bolt","Real-time analytics","See visits, events and conversions as they happen.","#"),
("ti-file-analytics","Page analytics","Track the performance of every page, entry and exit.","#"),
("ti-search","Site search analytics","See exactly what visitors search for on your site.","#")]),
("acquisition","Acquisition & marketing",[
("ti-route","Acquisition analytics","Which channels and campaigns drive quality traffic.","#"),
("ti-affiliate","Marketing attribution","Credit every channel fairly, cookieless.","#"),
("ti-robot","AI traffic analytics","Track visits from ChatGPT, Gemini and other LLMs.","#"),
("ti-player-play","Media analytics","Measure video and audio plays and engagement.","#")]),
("behaviour","Behaviour & conversion",[
("ti-activity","Behavioral analytics","Understand what visitors do, not just how many.","#"),
("ti-flame","Heatmaps","See clicks, scrolls and attention on every page.","1-feature-landing-heatmaps.html"),
("ti-device-desktop","Session recordings","Replay real sessions to find friction fast.","#"),
("ti-forms","Form analytics","Cut form abandonment with field-level insight.","#"),
("ti-filter","Funnel analysis","Find exactly where visitors drop out of funnels.","#"),
("ti-arrows-split-2","A/B testing","Test changes and measure the impact on revenue.","#"),
("ti-target","Conversion tracking","Track goals and conversions across the journey.","#")]),
("audience","Audience & journey",[
("ti-map-2","Customer journey analytics","Map every step from first visit to conversion.","#"),
("ti-users-group","Audience segmentation","Segment visitors to find your best audiences.","#")]),
("collect","Collect & integrate",[
("ti-tags","Tag Manager","Manage tags and triggers without touching code.","#"),
("ti-pointer","Event tracking","Capture custom events and interactions.","#")]),
("privacy","Privacy & platform",[
("ti-shield-check","GDPR-compliant analytics","Compliant by design, consent-free where possible.","2-vs-page-google-analytics.html"),
("ti-heartbeat","HIPAA-compliant analytics","Privacy-grade analytics for healthcare.","#"),
("ti-brand-open-source","Open-source analytics","100% open source, no black box, no lock-in.","#"),
("ti-cloud","Cloud or on-premise","Self-host, or use EU-based Matomo Cloud.","#")])]
def featurehub(groups):
    nav="".join(f'<a href="#{gid}">{name}</a>' for gid,name,_ in groups)
    secs=""
    for gid,name,items in groups:
        cards="".join(f'<a class="fhcard" href="{href}"><div class="ic"><i class="ti {ic}"></i></div><div><h3>{n}</h3><p>{d}</p></div></a>' for ic,n,d,href in items)
        secs+=f'<div id="{gid}" style="scroll-margin-top:130px;"><div class="fhcat"><h2>{name}</h2><span class="n">{len(items)} features</span></div><div class="fhgrid">{cards}</div></div>'
    return f'<div class="fhnav"><div class="row">{nav}</div></div><section class="section"><div class="wrap">{secs}</div></section>'
pages['9-features-hub.html']=shell(
"All Matomo Features, One Privacy-First Platform | Matomo",
"Explore every Matomo feature in one place: web analytics, heatmaps, A/B testing, funnels, attribution, tag manager and more, all privacy-first and fully owned.",
'<section class="hero" style="padding:78px 0 28px;"><div class="wrap"><span class="eyebrow">Product features</span><h1 style="max-width:720px;">Everything you need, in one privacy-first platform'+A_FHUB+'</h1><p class="lead" style="max-width:600px;">From web analytics to heatmaps, A/B testing and attribution, every Matomo feature in one place, with 100% data ownership.</p></div></section>'
+ featurehub(FEATURE_GROUPS)
+ callout("See it all on your own data","Start a free 21-day trial, no credit card, and explore every feature live.","Start your free trial"))

for fn,html in pages.items():
    with open(os.path.join(DIR,fn),'w') as f: f.write(html)
print("wrote",len(pages),"templates:",", ".join(pages.keys()))
