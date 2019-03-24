import re

multi_line = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>放弃不难，但坚持一定很酷——为梦想励志经典语录</title>
<meta name="keywords" content="放弃,不难,但,坚持,一定,很,酷,—,为,梦想,我," />
<meta name="description" content="我走得很慢，但绝不回头 放弃不难，但坚持一定很酷 希望在20出头的年纪里，做一件到80岁想起来还会骄傲的事 没有比脚更长的路，没有比人更高的山 他们想把我埋了，不知道 我却是" />
<meta name="applicable-device" content="pc">
<meta name="mobile-agent" content="format=html5;url=http://m.yikexun.cn/lizhi/qianming/20190341252.html">
<meta name="mobile-agent" content="format=xhtml; url=http://m.yikexun.cn/lizhi/qianming/20190341252.html">
<meta name="mobile-agent" content="format=wml; url=http://m.yikexun.cn/lizhi/qianming/20190341252.html">
<meta http-equiv="Cache-Control" content="no-transform" />
<link href="/static/css/css.css?v=20160105" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
<script type="text/javascript" src="/static/js/jquery.slide.js"></script>
<script type="text/javascript" src="/static/js/base.js?v=20160105"></script>
<script type="text/javascript" src="/js/a.js"></script>
</head>
<body>
<div class="topbar">
	<div class="area">
		<div class="i-ditu fl">一点点语录网 - 每天发现一点点</div>
		<div class="i-ditu fr">
			<a href="/data/sitemap.html">网站地图</a> - <a href="/data/baidunews.xml">最新更新</a> - <a href="/data/rssmap.html">RSS订阅</a>
		</div>
	</div>
</div>
<!-- header -->
<div class="header">
	<div class="area">
	<div class="logo tx fl"><a href="/" title="一点点语录网">一点点语录网</a></div>
	<div class="biaoyu tx fl">每天发现一点点！</div>
		<div class="site-search fr">
		<script type="text/javascript">(function(){document.write(unescape('%3Cdiv id="bdcs"%3E%3C/div%3E'));var bdcs = document.createElement('script');bdcs.type = 'text/javascript';bdcs.async = true;bdcs.src = 'http://znsv.baidu.com/customer_search/api/js?sid=4510295353417073839' + '&plate_url=' + encodeURIComponent(window.location.href) + '&t=' + Math.ceil(new Date()/3600000);var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(bdcs, s);})();</script>
		</div>
	</div>
</div>
<!-- Nav -->
<div class="nav">
		<div class="area">
		<ul id="nav" class="navbar f14">
		<li class="current on"><h3><a href="/">首页</a></h3></li>
		<li class="current">
			<h3><a href="/yulu/">经典语录</a></h3>
			<div class="nav-sub-icon"></div>
			<div class="drop par yl">
				<div class="yl-info">
					<a href="/niandujingdianyulu/2013yulu/">2018经典语录</a>
					<a href="/mingrenjingdianyulu/">名人经典语录</a>
					<a href="/niandujingdianyulu/">年度经典语录</a>
					<a href="/aiqingyulu/">爱情语录</a>
					<a href="/jingdiangaoxiaoyulu/">经典搞笑语录</a>
					<a href="/hanhan/">韩寒经典语录</a>
					<a href="/guojingming/">郭敬明经典语录</a>
					<a href="/zhangailing/">张爱玲经典语录</a>
					<a href="/zhangxiaoxian/">张小娴经典语录</a>
				</div>
			</div>
		</li>
		<li class="current">
			<h3><a href="/mrmy/">名人名言</a></h3>
			<div class="nav-sub-icon"></div>
			<div class="drop ver">
				<a href="/mrmy/lizhi/">励志名言</a>
				<a href="/mrmy/rensheng/">人生格言</a>
				<a href="/mrmy/dushu/">读书名言</a>
				<a href="/mrmy/aiqing/">爱情名言</a>
				<a href="/mrmy/aiguo/">爱国名言</a>
			</div>
		</li>
		<li class="current">
			<h3><a href="/jingdiantaici/">经典台词</a></h3>
		</li>
		<li class="current">
			<h3><a href="http://juzi.yikexun.cn" target="_blank">句子大全</a></h3>
		</li>
		<li class="current">
			<h3><a href="/lizhi/">励志</a></h3>
			<div class="nav-sub-icon"></div>
			<div class="drop ver"><a href="/lizhi/qianming/">励志签名</a></div>
		</li>
		<li class="current">
			<h3><a href="/rensheng/">人生</a></h3>
			<div class="nav-sub-icon"></div>
			<div class="drop ver"><a href="/rensheng/ganwu/">人生感悟</a></div>
		</li>
		<li class="current">
			<h3><a href="/zuowen/">作文</a></h3>
			<div class="nav-sub-icon"></div>
			<div class="drop par zw">
				<div class="zw-info">
					<a href="/zuowen/xiao/">小学作文</a>
					<a href="/zuowen/zhong/">初中作文</a>
					<a href="/zuowen/gao/">高中作文</a>
					<a href="/zuowen/jie/">节日作文</a>
					<a href="/zuowen/jing/">写景作文</a>
				</div>
			</div>
		</li>
		<li class="current">
			<h3><a href="/shi/">诗句</a></h3>
		</li>
		<li class="current">
			<h3><a href="javascript:;" title="更多">更多</a></h3>
			<div class="nav-sub-icon"></div>
			<div class="drop ver">
				<a href="/t/">热门推荐</a>
				<a href="/suibi/">情感日志</a>
				<a href="/jingdianduanxin/">经典短信</a>
				<a href="/duhougan/">读后感</a>
				<a href="/duanzi/">段子</a>
				<a href="/QQ/">QQ个性</a>
				<a href="/yule/">娱乐</a>
			</div>
		</li>
		</ul>
		<script type="text/javascript">jQuery("#nav").slide({ type:"menu",titCell:".current",targetCell:".drop",effect:"slideDown",delayTime:300,triggerTime:0,returnDefault:true});</script>
		<div class="clear"></div>
	    </div>
</div>
<div class="clear blank15"></div>
<div class="clear blank15"></div>
<div class="area">
	<div class="nowsite">
		<div class="place fl">当前位置：<a href='http://www.yikexun.cn/'>一点点</a> > <a href='/lizhi/'>励志</a> > <a href='/lizhi/qianming/'>励志签名</a> > </div>
		<div class="ad-box650txt fr"></div>
	</div>
	<!-- art-main -->
	<div class="art-main fl">
		<div class="arc-box be">
			<!-- title -->
			<div class="arc-title">
				<h1>放弃不难，但坚持一定很酷——为梦想励志经典语录</h1>
				<div class="info">
					<span>分类：励志签名</span>
					<span>时间：2019-03-21</span>
				</div>
			</div>
			<!-- content -->
			<div class="arc-content">
				<table>
				<tbody><tr>
				<td>
				<!-- ad -->
				<div class="ad-box650"></div>
				<!-- neirong -->
				<div class="neirong">
					<ol class=" list-paddingleft-2" style="list-style-type: decimal;"><li><p>我走得很慢，但绝不回头</p></li><li><p>放弃不难，但坚持一定很酷<br/></p></li><li><p>希望在20出头的年纪里，做一件到80岁想起来还会骄傲的事<br/></p></li><li><p>没有比脚更长的路，没有比人更高的山<br/></p></li><li><p>他们想把我埋了，不知道 我却是种子<br/></p></li><li><p>别总羡慕别人的光鲜亮丽，那只是你没有看到他们背后默默付出的努力。<br/></p></li><li><p>成长总是伴随着汗水与眼泪，要走更长远的路，就要有异于常人的付出。<br/></p></li><li><p>如果你一生只有一次翻身的机会，那你就要用尽全力 我的青春，无问西东<br/></p></li><li><p>多数人认为勇气就是不害怕。现在让我来告诉你，不害怕不是勇气，它是某种脑损伤。勇气是尽管你感觉害怕，但仍能迎难而上；尽管你感觉痛苦，但仍能直接面对。<br/></p></li><li><p>天上不会掉馅饼 努力奋斗才能梦想成真<br/></p></li><li><p>“任何事情都会有皆大欢喜的结果，如果没有，就证明还没有到最后。”<br/></p></li><li><p>“当你感到累的时候，其实你是在走上坡路”<br/></p></li><li><p>我始终相信那些历尽劫数 走过平湖烟雨 岁月山河 尝遍百味的人会更加生动而干净。<br/></p></li><li><p>“你的任务，就是珍惜你自己的人生。而且还要比之前更加珍惜。”<br/></p></li><li><p>一味沉湎于过去是毫无意义的。一直看着后视镜是很危险的，会出交通事故哦。开车的时候必须专心地看着前进的方向。已经走过的路，只要时不时回顾一下就可以了。<br/></p></li><li><p>“没事的，每个人大概都会经历一些情绪崩溃或者极端的时刻，会好的，会熬过来的。”愿你昨晚睡前的坏情绪 在今日清晨掀开被子 拉开窗帘的那一刻 杳无踪影<br/></p></li><li><p>一个人只拥有此生此世是不够的，他还应该拥有诗意的世界。<br/></p></li><li><p>一定要努力活下去，因为有美好的人生在等着你。<br/></p></li><li><p>有时候会讨厌不甘平庸却又不好好努力的自己，觉得自己不够好，羡慕别人闪闪发光，但其实大多人都是普通的，只是别人的付出你没看到。不要沮丧，不必惊慌，做努力爬的蜗牛或坚持飞的笨鸟，我们试着长大，一路跌跌撞撞，然后遍体鳞伤。坚持着，总有一天，你会站在最亮的地方，活成自己曾经渴望的模样。<br/></p></li><li><p>一个人要经历过漫长的岁月，才能培养出年轻的心。<br/></p></li><li><p>尽管我的道路从头到尾都长满了杂草，但也只有我自己是我这一生的见证人。<br/></p></li><li><p>如果你的行为散发的是快乐，就不可能在心理上保持忧郁。<br/></p></li><li><p>爱钱就说出来，知道目标一定会达成，相信自己就是那种人，强调自己一定会好运，事情就会向你希望的方向发展，屡试不爽。<br/></p></li><li><p>逆风的方向更适合飞翔，我不怕千万人阻挡只怕自己投降</p><p><img title="211553169693562416.jpg" alt="v2-300bf0b03b08b1f5d0bfe637c6cfdada_r.jpg" src="/uploads/image/201903/211553169693562416.jpg"/><br/></p></li></ol>
				</div>
				</td>
				</tr>
				</tbody></table>
			</div>
			<!-- tuijian -->
			<div class="tuijian">
				<ul>
				<li><a href="/lizhi/qianming/20190141207.html" title="成功的道路并不拥挤，别那么早放弃——年轻人必读的经典励志">成功的道路并不拥挤，别那么早放弃——年轻人必读的经典励志</a></li>
<li><a href="/lizhi/qianming/20190141188.html" title="人生有时很难但愿你学会坚强——告诫年轻人的经典励志语录">人生有时很难但愿你学会坚强——告诫年轻人的经典励志语录</a></li>
<li><a href="/lizhi/qianming/20181241081.html" title="比你优秀的人还在努力——激励自己，不放弃的经典语录">比你优秀的人还在努力——激励自己，不放弃的经典语录</a></li>

				</ul>
			</div>
			<!-- page -->
			<div class="arc-page">
				<ul class="pagelist">
				
				</ul>
			</div>
			<!-- fenxiang -->
			<div class="fenxiang">
				<div class="bdsharebuttonbox fl">
					<a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a>
					<a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a>
					<a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a>
					<a href="#" class="bds_renren" data-cmd="renren" title="分享到人人网"></a>
					<a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a>
					<a href="#" class="bds_douban" data-cmd="douban" title="分享到豆瓣网"></a>
					<a href="#" class="bds_bdhome" data-cmd="bdhome" title="分享到百度新首页"></a>
					<a href="#" class="bds_tieba" data-cmd="tieba" title="分享到百度贴吧"></a>
					<a href="#" class="bds_more" data-cmd="more"></a>
				</div>
				<div class="aspl fr"></div>
			</div>
		</div>
		<div class="blank10"></div>
		<!-- xiangguan -->
		<div class="info-box be">
			<div class="news-mod-t"><h3>放弃不难，但坚持一定很酷——为梦想励志经典语录相关文章</h3></div>
			<ul class="news-ul xg py10">
			<li><a href="/lizhi/qianming/20190141207.html" target="_blank">成功的道路并不拥挤，别那么早放弃——年轻人必读的经典励志</a></li>
<li><a href="/lizhi/qianming/20190141188.html" target="_blank">人生有时很难但愿你学会坚强——告诫年轻人的经典励志语录</a></li>
<li><a href="/lizhi/qianming/20181241081.html" target="_blank">比你优秀的人还在努力——激励自己，不放弃的经典语录</a></li>
<li><a href="/lizhi/qianming/20181241012.html" target="_blank">没有容易的人生，只有不言放弃的你我——人生经典励志名言</a></li>
<li><a href="/lizhi/qianming/20181141000.html" target="_blank">你的房子是租的，但生活不是。——送给为生活而奋斗的你</a></li>
<li><a href="/lizhi/qianming/20180340764.html" target="_blank">优美的励志文章(1)跌倒了不要紧,但要记得爬起来</a></li>
<li><a href="/lizhi/qianming/20180139718.html" target="_blank">人可以没有骨气，但不可以做懦夫</a></li>
<li><a href="/lizhi/qianming/20180139714.html" target="_blank">努力，奋斗，坚持，不抛弃，不放弃，一切皆有可能</a></li>
<li><a href="/lizhi/qianming/20170938449.html" target="_blank">对自己说声谢谢，在最苦最累的时候没有放弃！</a></li>
<li><a href="/lizhi/qianming/20170736523.html" target="_blank">喜欢就该珍惜，珍惜就别放弃</a></li>
<li><a href="/lizhi/qianming/20170635677.html" target="_blank">跪着，虽不会跌倒，但可能被践踏</a></li>
<li><a href="/lizhi/qianming/20170634734.html" target="_blank">青春的励志签名</a></li>

			</ul>
		</div>
		<!-- ad -->
		<div class="ad-box be p10">
			<div class="ad-box650"></div>
		</div>
		<div class="blank10"></div>
		<!-- hot -->
		<div class="info-box be">
			<div class="news-mod-t"><h3>热门推荐</h3></div>
			<ul class="news-ul xg py10">
			<li><a href="/lizhi/qianming/20190341252.html" target="_blank">放弃不难，但坚持一定很酷——为</a></li>
<li><a href="/lizhi/qianming/20190341250.html" target="_blank">乾坤未定，你我皆是黑马 ——关于</a></li>
<li><a href="/lizhi/qianming/20190241246.html" target="_blank">我不知道年少轻狂，我只知道胜者</a></li>
<li><a href="/lizhi/qianming/20190241243.html" target="_blank">最痛苦的事不是失败 而是你本可以</a></li>
<li><a href="/lizhi/qianming/20190241240.html" target="_blank">只有非常努力才能看起来毫不费劲</a></li>
<li><a href="/lizhi/qianming/20190241232.html" target="_blank">要么出众，要么出局——令人深思</a></li>
<li><a href="/lizhi/qianming/20190241231.html" target="_blank">当你感到累的时候，其实你是在走</a></li>
<li><a href="/lizhi/qianming/20190141227.html" target="_blank">不疯狂的梦想没有实现的意义——</a></li>
<li><a href="/lizhi/qianming/20190141224.html" target="_blank">人生没有白走的路，每一步都算数</a></li>
<li><a href="/lizhi/qianming/20190141222.html" target="_blank">坚持下去为了想要的人生——正能</a></li>
<li><a href="/lizhi/qianming/20190141219.html" target="_blank">你的努力永远不会背叛你——句句</a></li>
<li><a href="/lizhi/qianming/20190141216.html" target="_blank">你长大后想成为什么样的人？——</a></li>
<li><a href="/lizhi/qianming/20190141211.html" target="_blank">要想人前显贵，必得人后受罪——</a></li>
<li><a href="/lizhi/qianming/20190141207.html" target="_blank">成功的道路并不拥挤，别那么早放</a></li>
<li><a href="/lizhi/qianming/20190141205.html" target="_blank">走出舒适区——激励人心追求梦想</a></li>
<li><a href="/lizhi/qianming/20190141201.html" target="_blank">在自己的人生里做主角——激情人</a></li>
<li><a href="/lizhi/qianming/20190141198.html" target="_blank">不怕失败才是成功的开始——不妥</a></li>
<li><a href="/lizhi/qianming/20190141194.html" target="_blank">一定是那些艰难时刻成就我们——</a></li>

			</ul>
		</div>
		<div class="blank10"></div>
		<!-- hot -->
		<div class="info-box be">
			<div class="news-mod-t"><h3>其他推荐</h3></div>
			<ul class="news-ul xg py10">
			<li><a href="/t/1112/2791.html" target="_blank">描写江南的诗句</a></li>
<li><a href="/t/1112/2781.html" target="_blank">描写柳树的诗句</a></li>
<li><a href="/t/1112/2771.html" target="_blank">描写明月的诗句</a></li>
<li><a href="/t/1112/2761.html" target="_blank">描写母爱的诗句</a></li>
<li><a href="/t/1112/2751.html" target="_blank">描写沙漠的诗句</a></li>
<li><a href="/t/1112/2741.html" target="_blank">描写山水的诗句</a></li>
<li><a href="/t/1112/2731.html" target="_blank">描写树的诗句</a></li>
<li><a href="/t/1112/2721.html" target="_blank">描写四季的诗句</a></li>
<li><a href="/t/1112/2711.html" target="_blank">描写太阳的诗句</a></li>
<li><a href="/t/1112/2701.html" target="_blank">描写夕阳的诗句</a></li>
<li><a href="/t/1112/2691.html" target="_blank">描写小草的诗句</a></li>
<li><a href="/t/1112/2681.html" target="_blank">描写友情的诗句</a></li>
<li><a href="/t/1112/2671.html" target="_blank">描写友谊的诗句</a></li>
<li><a href="/t/1112/2661.html" target="_blank">描写山水的诗句</a></li>
<li><a href="/t/1112/2621.html" target="_blank">描写荷花的诗句</a></li>
			</ul>
		</div>
	</div>
	<!-- art-side -->
	<div class="art-side fr">
		<!-- news -->
		<div class="news-mod">
			<div class="news-mod-t"><h3>关注排行</h3></div>
			<ul class="news-ul">
			<li><a href="/lizhi/qianming/20150925011.html" target="_blank">30条经典励志语录：我经得起多少诋毁，就担得起多少赞美</a></li>
<li><a href="/lizhi/qianming/20150324710.html" target="_blank">一句话经典励志语录：用最真实的自己，才能遇见最应该的那个</a></li>
<li><a href="/lizhi/qianming/20141124344.html" target="_blank">2014年的经典励志语录：最怕你一生碌碌无为，还安慰自己平凡可</a></li>
<li><a href="/lizhi/qianming/20150324713.html" target="_blank">20条经典励志语录：我们要在安静中，不慌不忙地刚强。</a></li>
<li><a href="/lizhi/qianming/20121220539.html" target="_blank">82句经典一句话励志签名：跌下去是耻辱，站起来是尊严。</a></li>
<li><a href="/lizhi/qianming/20141024280.html" target="_blank">44条值得收藏的经典励志语录：只要我们能梦想的，我们就能实</a></li>
<li><a href="/lizhi/qianming/20140924233.html" target="_blank">58条超赞的一句话经典励志语录：你不勇敢，没人替你坚强。</a></li>
<li><a href="/lizhi/qianming/20121018592.html" target="_blank">50句关于励志的经典句子，句句经典！</a></li>
<li><a href="/lizhi/qianming/20121018095.html" target="_blank">励志：别怕输不起，一切都来得及！</a></li>
<li><a href="/lizhi/qianming/20141024248.html" target="_blank">28条正能量经典语录：之所以痛苦一是求之不得，二是舍之不得</a></li>

			</ul>
		</div>
		<div class="blank10"></div>
		<!-- ad:300*280 -->
		<div class="overflow">
			<script type="text/javascript">content_300_1();</script>
		</div>
		<div class="blank10"></div>
		<!-- news -->
		<div class="news-mod">
			<div class="news-mod-t"><h3>最新更新</h3></div>
			<ul class="news-ul">
			<li><a href="/lizhi/qianming/20130822459.html" target="_blank">32条励志语录：寒冷到了极致时，太阳就要光临</a></li>
<li><a href="/lizhi/qianming/20190141176.html" target="_blank">没有努力过的人，不配谈运气——30句回味一天的励志语录</a></li>
<li><a href="/lizhi/qianming/20170533018.html" target="_blank">经商励志名言 生命因诚信而美丽</a></li>
<li><a href="/lizhi/qianming/20170532786.html" target="_blank">一些正能量的话</a></li>
<li><a href="/lizhi/qianming/20170533301.html" target="_blank">宋思明经典励志语录</a></li>
<li><a href="/lizhi/qianming/20120917975.html" target="_blank">最新励志签名：昨天，永远属于过去，展望未来，要有实力</a></li>
<li><a href="/lizhi/qianming/20181241112.html" target="_blank">世界上唯一可以不劳而获的就是贫穷——句句走心励志语录</a></li>
<li><a href="/lizhi/qianming/20121018125.html" target="_blank">只要心中有希望存在，就有幸福存在</a></li>

			</ul>
		</div>
		<!-- ad:300*250 -->
		<div id="fixed" class="overflow">
			<script type="text/javascript">content_300_2();</script>
		</div>
	</div>
</div>
<div class="clear blank15"></div>
<div class="footer">
	<div class="area">
	<p class="i-info"><a href="http://www.yikexun.cn" target="_blank">网站首页</a><span class="sep">|</span><a href="/data/sitemap.html" target="_blank">网站地图</a><span class="sep">|</span><a href="http://m.yikexun.cn">手机浏览</a></p>
	<p><a href="http://www.miibeian.gov.cn/" target="_blank" rel="nofollow">豫ICP备12014623号</a></p>
	<p>©Copyright 2010-2016 一点点语录网 www.yikexun.cn All Rights Reserved </p>
	</div>
</div>
<!-- adm:xuanfu -->
<script type="text/javascript" src="/js/pv.js"></script>
<!-- tongji -->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?bd8642aa2cf782adfd2fdbda29992d5c";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
<!-- tui -->
<script>
(function(){
    var bp = document.createElement('script');
    bp.src = '//push.zhanzhang.baidu.com/push.js';
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
<!-- js -->
<!-- fenxiang -->
<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"32"},"share":{},"image":{"viewList":["qzone","tsina","tqq","renren","weixin","bdhome","tieba"],"viewText":"分享到：","viewSize":"16"}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
<!-- count -->
<script src="http://go.yikexun.cn/addArcHits.php?id=41252" type='text/javascript' language="javascript"></script>
<script type="text/javascript">$("#fixed").smartFloat();</script>
</body>
</html>
'''

pattern = re.compile(r'<div class="neirong">.*?<ol .*?>(.*?)</ol>.*?</div>',re.S)

ret = pattern.findall(multi_line)

print(ret)

string = '<img title="211553169693562416.jpg" alt="v2-300bf0b03b08b1f5d0bfe637c6cfdada_r.jpg" ' \
         'src="/uploads/image/201903/211553169693562416.jpg"/> '

pattern = re.compile(r'<li .*?></li>')

ret = pattern.sub(' ',multi_line)

print(ret)

