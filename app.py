import streamlit as st

# 你的表白爱心烟花 HTML 代码
html_code = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>浪漫告白</title>
<style>
  *{margin:0;padding:0;box-sizing:border-box;}
  body{
    background:#000;
    overflow:hidden;
    height:100vh;
    cursor:pointer;
  }
  .heart{
    position:absolute;
    width:22px;
    height:22px;
    background:#ff8fab;
    transform:rotate(45deg);
    animation:float 3s infinite;
    box-shadow:0 0 15px #ff8fab;
  }
  .heart:before,.heart:after{
    content:'';
    position:absolute;
    width:22px;
    height:22px;
    background:#ff8fab;
    border-radius:50%;
    box-shadow:0 0 15px #ff8fab;
  }
  .heart:before{left:-11px;}
  .heart:after{top:-11px;}
  @keyframes float{
    0%{opacity:0;transform:rotate(45deg) translateY(0);}
    20%{opacity:1;}
    100%{opacity:0;transform:rotate(45deg) translateY(-800px);}
  }
  .firework{
    position:absolute;
    width:10px;
    height:10px;
    background:#ff5c8d;
    transform:rotate(45deg);
    pointer-events:none;
    animation:firework 1s forwards;
    box-shadow:0 0 10px #ff5c8d;
  }
  .firework:before,.heart:after{
    content:'';
    position:absolute;
    width:10px;
    height:10px;
    background:#ff5c8d;
    border-radius:50%;
  }
  .firework:before{left:-5px;}
  .firework:after{top:-5px;}
  @keyframes firework{
    0%{opacity:1;transform:rotate(45deg) scale(1);}
    100%{opacity:0;transform:rotate(45deg) scale(3);}
  }
  .text{
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    font-size:58px;
    color:#fff;
    font-weight:bold;
    text-shadow:0 0 15px #ff8fab,0 0 30px #ff5c8d,0 0 45px #ff2e63;
    white-space:nowrap;
    font-family:"Microsoft YaHei",sans-serif;
  }
</style>
</head>
<body>
  <div class="text">世水长流 直到永远</div>
  <script>
    function createHeart(){
      const heart=document.createElement('div');
      heart.classList.add('heart');
      heart.style.left=Math.random()*window.innerWidth+'px';
      heart.style.animationDuration=(Math.random()*2+1)+'s';
      document.body.appendChild(heart);
      setTimeout(()=>{heart.remove();},3000);
    }
    setInterval(createHeart,120);
    document.addEventListener('click',(e)=>{
      for(let i=0;i<12;i++){
        setTimeout(()=>{
          const fire=document.createElement('div');
          fire.classList.add('firework');
          fire.style.left=e.clientX + (Math.random()-0.5)*120 +'px';
          fire.style.top=e.clientY + (Math.random()-0.5)*120 +'px';
          document.body.appendChild(fire);
          setTimeout(()=>{fire.remove();},1000);
        },i*80);
      }
    });
  </script>
</body>
</html>
"""

# Streamlit 核心：展示 HTML
st.components.v1.html(html_code, height=700, scrolling=False)