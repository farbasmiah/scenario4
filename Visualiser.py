import math
import matplotlib.pyplot as plt

def equation (x1,y1,x2,y2):
    if x1==x2:
        return (y1,0)
    x1 += 0.0
    grad = (y2-y1)/(x2-x1)
    cons = y1 - (x1 * grad)
    return (grad,cons)

def intersection (fst,snd):
    if fst[0] == snd[0]:
        print "erro"
        return False
    x = fst[0] - snd[0]
    c = snd[1] - fst[1] + 0.0
    c = c/x
    return c

#xs = (0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (3, 2), (3, 3), (0, 3)
xs = (1.595280923702749, -18.738628088850852), (1.154623844327566, -18.000071179188005), (0.8281725642223983, -18.79573098848586), (0.44461838448222313, -18.824282438303364), (0.0039613051070399585, -18.085725528640516), (-0.3224899749981276, -18.881385337938372), (-0.7060441547383034, -18.909936787755875), (-1.1467012341134861, -18.171379878093028), (-1.7370183278238223, -18.79681628516219), (-2.1052563093935546, -18.685776729091888), (-2.251415178822683, -17.838261209882123), (-2.8417322725330187, -18.463697616951286), (-3.209970254102751, -18.352658060880984), (-3.35612912353188, -17.505142541671216), (-3.946446217242216, -18.13057894874038), (-4.314684198811948, -18.019539392670076), (-4.4608430682410765, -17.17202387346031), (-5.236331519498113, -17.543860709157318), (-5.540163944028324, -17.308032695793905), (-5.372340341831708, -16.464539833370072), (-6.147828793088745, -16.836376669067082), (-6.451661217618955, -16.60054865570367), (-6.28383761542234, -15.757055793279832), (-7.059326066679377, -16.128892628976843), (-7.363158491209587, -15.89306461561343), (-7.195334889012972, -15.049571753189595), (-8.052615272586577, -15.118239899764935), (-8.251538607931435, -14.78906137565056), (-7.792104895047544, -14.062036180846471), (-8.64938527862115, -14.130704327421812), (-8.848308613966006, -13.801525803307438), (-8.388874901082115, -13.07450060850335), (-9.246155284655721, -13.143168755078689), (-9.445078620000578, -12.813990230964315), (-8.985644907116686, -12.086965036160226), (-9.810434214444648, -11.843310426247621), (-9.877930231945196, -11.464663781333917), (-9.188132959618336, -10.951025101419111), (-10.012922266946298, -10.707370491506506), (-10.080418284446848, -10.328723846592801), (-9.390621012119988, -9.815085166677994), (-10.21541031944795, -9.571430556765389), (-10.2829063369485, -9.192783911851684), (-9.593109064621638, -8.679145231936879), (-9.403493371850793, -7.69728684649882), (-9.0767761860275, -8.642408997592376), (-8.321269727704788, -9.297550197207144), (-7.339411342266727, -9.487165889977987), (-9.09651288753321, -10.442463832832537), (-8.618863916105935, -11.321014605465779), (-7.940764044075677, -11.521465506068763), (-7.224290586934764, -12.839291665018624), (-7.424741487537748, -13.517391537048884), (-5.552519186939304, -15.914219369234972), (-6.5461907149045055, -13.039742565621609), (-7.740313143472694, -10.843365634038504), (-6.861762370839452, -10.365716662611229), (-5.88669870925007, -12.159173750347005), (-6.394289191173172, -9.160448704154694), (-4.883276274527752, -10.470731103384228), (-4.228135074912986, -9.715224645061518), (-5.739147991558405, -8.404942245831984), (-5.215651925796964, -7.722595677329956), (-4.838014085243865, -7.795524789934126), (-4.606234469899106, -8.623729583644497), (-4.082738404137665, -7.941383015142467), (-3.7051005635845655, -8.014312127746637), (-3.4733209482398064, -8.842516921457008), (-2.949824882478365, -8.160170352954978), (-2.572187041925266, -8.23309946555915), (-2.3404074265805073, -9.061304259269521), (-1.4920622834316548, -9.590747852200584), (-1.0431212475214078, -10.324298747974037), (-1.2467533986487396, -10.650585341492826), (-2.10295873681365, -10.569607632756952), (-1.6540177009034032, -11.303158528530405), (-1.857649852030735, -11.629445122049194), (-2.7138551901956456, -11.54846741331332), (-2.2649141542853983, -12.282018309086773), (-2.46854630541273, -12.608304902605564), (-3.324751643577641, -12.527327193869688), (-2.680038651556118, -13.383057380319542), (-0.11427354735173934, -9.271846301982794), (-1.8109638336494447, -8.212959116120668), (-1.773153893256564, -8.15237498643563), (-2.3333540735870413, -7.324017721749854), (-0.1283823696949531, -5.229238548415534), (-2.893554253917519, -6.495660457064078), (-2.9615179322573866, -6.395163869122275), (-2.108247314788589, -1.9768011346510077), (-0.013468141454267002, -4.181772838543095), (-1.2798900501028136, -1.4166009543205296), (-0.3510361974752334, -0.7884370956501838), (-0.2731183118817338, 2.2519459070494166), (-1.332894582913293, -0.5988214028793406), (-0.5744318118299201, 3.3286121388728978), (1.3158124903571917, 3.982046510519487), (2.02113631932593, 4.03222913987346), (3.1543960068099963, 3.049517340451312), (3.204578636163971, 2.344193511482575), (3.8597198357787352, 3.099699969805287), (1.9709536899719566, 4.7375529688421985), (6.235611338292703, 2.1274389593362217), (6.40106570217418, 1.4399617935535494), (3.581259712231135, 2.57956443442506), (5.879042900272985, 0.5870302638894002), (5.618031499322387, 0.16056449905732562), (4.930554333539715, -0.004889864824151324), (5.783485863203864, -0.5269126667253468), (7.088542867956852, 1.6054161574350263), (7.159133639522987, 1.5622122294763177), (2.6260948895867244, 5.493059427164913), (3.005326275128411, 7.456776198041034), (2.35189190348182, 9.347020500228144), (5.627597901555646, 13.1245527918417), (4.872091443232934, 13.779693991456465), (1.5963854451591093, 10.00216169984291), (0.8408789868363968, 10.657302899457676), (-1.1228377840397241, 11.036534284999359), (-3.013082086226837, 10.38309991335277), (-4.323364485456366, 8.872086996707347), (-4.702595870998052, 6.908370225831227), (-4.049161499351464, 5.018125923644117), (-2.5381485827060395, 3.707843524414584), (-4.718729049570742, -7.583527908123098), (-5.549532298787561, -7.423083860393922), (-5.876249484610855, -6.477961709300366), (-6.631755942933566, -5.8228205096856005), (-7.613614328371625, -5.6332048169147555), (-8.46629182376024, -5.5210172094351515), (-8.591952279846122, -5.157508689783785), (-7.990595696629271, -4.542679257960653), (-8.843273192017886, -4.43049165048105), (-8.968933648103768, -4.0669831308296835), (-8.367577064886916, -3.4521536990065522), (-9.220254560275531, -3.3399660915269482), (-9.345915016361413, -2.9764575718755815), (-8.74455843314456, -2.3616281400524506), (-8.463559568201033, -1.5488030615056263), (-8.082229763793599, -1.4986375917736718), (-7.600569019922255, -2.211131730856587), (-7.319570154978729, -1.398306652309763), (-6.938240350571295, -1.3481411825778085), (-6.45657960669995, -2.0606353216607243), (-6.175580741756424, -1.2478102431138995), (-5.794250937348989, -1.1976447733819453), (-5.312590193477645, -1.910138912464861), (-5.061690610373292, -0.8685159512735747), (-8.874988654447641, -1.3701706485931195), (-9.005418875750722, -0.3787131571337887), (-8.724420010807195, 0.43411192141303545), (-8.343090206399761, 0.4842773911449897), (-7.861429462528418, -0.22821674793792598), (-7.580430597584892, 0.5846083306088982), (-7.199100793177457, 0.6347738003408527), (-6.717440049306113, -0.07772033874206324), (-6.436441184362586, 0.7351047398047612), (-6.055111379955151, 0.7852702095367154), (-5.573450636083807, 0.07277607045379947), (-3.6290622077875945, -0.3955759765234545), (-3.3948861842989673, 0.576618237624652), (-5.33927461259518, 1.0449702846019058), (-5.322551052979454, 1.1143990316450854), (-6.314008544438785, 0.9839688103420045), (-7.435896257201197, 1.8449960804982544), (-7.827186921110441, 4.819368554876247), (-6.96615965095419, 5.941256267638659), (-8.949074633872854, 5.6803958250324955), (-8.296923527357446, 0.7231083677358425), (-9.135849097053804, 0.6127443343255422), (-9.141246464625002, 0.653772099663692), (-9.743968674754143, -2.3272891102776674), (-9.815341040323997, -2.324836806224376), (-12.789706994738204, -1.9334965843947387), (-12.920153735348082, -2.924951902532807), (-9.945787780933875, -3.3162921243624446), (-10.039716255283206, -4.030191797001608), (-10.76673329458594, -4.281512709173371), (-11.9963921582322, -3.078799542739664), (-12.22076737319141, -4.7841545335168965), (-12.947784412494144, -5.035475445688659), (-14.177443276140405, -3.8327622792549523), (-14.401818491099615, -5.538117270032185), (-15.128835530402348, -5.789438182203947), (-16.35849439404861, -4.58672501577024), (-16.392833423823394, -5.586135257379824), (-16.803636616576913, -6.3417050471661245), (-17.18802517104214, -6.328497728021977), (-17.545999087219066, -5.54651329994738), (-17.95680227997259, -6.3020830897336815), (-18.34119083443781, -6.2888757705895335), (-18.69916475061474, -5.506891342514937), (-19.10996794336826, -6.262461132301238), (-19.494356497833486, -6.24925381315709), (-19.852330414010414, -5.467269385082493), (-19.97410656889985, -4.474711795770745), (-20.57584660726516, -3.676019786152447), (-21.496314771772894, -3.2852022352060124), (-22.48887236108464, -3.4069783900954476), (-23.28756437070294, -4.008718428460758), (-23.678381921649372, -4.92918659296849), (-23.556605766759937, -5.921744182280239), (-22.954865728394626, -6.720436191898536), (-22.034397563886895, -7.11125374284497), (-21.041839974575147, -6.989477587955537), (-20.243147964956847, -6.3877375495902236), (-20.271057998250424, -6.45347230754793), (-16.42717245359818, -6.585545498989408), (-16.43207706170476, -6.728290230129115), (-9.161906668677414, -4.2150811084114865), (-8.558736479465182, -5.959922002738049), (-9.213877679079948, -6.71542846106076), (-9.024261986309105, -5.7335700756227), (-10.006120371747164, -5.543954382851856), (-10.574967450059697, -8.489529539166034), (-10.645086358897823, -8.475988232524603), (-22.10788238920257, -12.550826532093033), (-10.294107067894963, -10.444950786075871), (-9.97012618389232, -12.262454681661657), (-10.040432405158917, -12.274987183942482), (-8.051199051710345, -15.566772425086222), (-8.112320148288056, -15.60370804360473), (-5.07399590298595, -17.961988177238858), (-5.117783895593593, -18.018403069471315), (-1.435404079896271, -19.12879863017433), (-1.4560216443281515, -19.19717219523499), (2.379520153073602, -18.91165769705995), (2.4329723488443173, -19.629723267641904), (1.7723869667409986, -20.023858941341675), (0.3235302372381357, -19.09682385083481), (0.45121620253436134, -20.81213028874122), (-0.20936917956895718, -21.20626596244099), (-1.6582259090718208, -20.279230871934125), (-1.530539943775595, -21.994537309840535), (-2.191125325878914, -22.38867298354031), (-3.6399820553817768, -21.46163789303344), (-3.275814685865687, -23.573295560201842), (3.3300391351674996, -19.631938823204123), (3.988779886610377, -20.736011709868), (13.490139939421907, -8.635989078509756), (14.341734262286593, -9.304690660893437), (10.296118078158603, -4.873777697324678), (10.348856637807327, -4.825625099384539), (6.90875205703842, -3.1055728090000843), (7.615384615384616, -1.692307692307692), (8.769230769230768, -1.6923076923076912), (9.923076923076923, -4), (11.076923076923077, -1.692307692307692), (11.576923076923077, -2.192307692307692), (11.576923076923077, -3.692307692307692), (11.076923076923077, -4.192307692307692), (12.076923076923077, -4.192307692307692), (12.076923076923077, -1.692307692307692), (12.23076923076923, -1.692307692307692), (13.384615384615383, -4), (13.743594463924252, -3.0666543937969406), (14.323483745884733, -3.701771226420324), (14.185414869227476, -4.060750305729194), (13.32938783395248, -4.143591631723548), (13.90927711591296, -4.7787084643469315), (13.771208239255703, -5.1376875436558), (12.915181203980708, -5.220528869650154), (13.495070485941188, -5.855645702273538), (13.357001609283932, -6.214624781582407), (12.500974574008936, -6.297466107576762), (13.29625130355474, -7.0154242661945005), (14.676940070127312, -3.42563347310581), (15.61028567633037, -3.784612552414679), (14.389756806680216, -9.743665268941905), (14.89729266175903, -8.882034631249967), (19.205445850218723, -11.419713906644034), (18.190374140061092, -13.14297518202791), (17.468565544734336, -13.610561882145243), (17.13716914562205, -13.415355784038006), (17.19618494272424, -12.5573568877062), (16.474376347397484, -13.024943587823532), (16.1429799482852, -12.829737489716296), (16.20199574538739, -11.971738593384492), (15.480187150060631, -12.439325293501822), (15.148790750948347, -12.244119195394587), (15.207806548050538, -11.386120299062782), (14.505297473431254, -11.305615640330776), (13.572290849600336, -10.13109504030384), (13.652795508332341, -9.428585965684556), (12.86978177498105, -10.050590381571837), (14.424792814699249, -12.00812471495006), (14.368874293859438, -12.052544838647485), (17.682838284982278, -14.004605819719849), (17.175302429903464, -14.86623645741179), (16.453493834576708, -15.333823157529121), (16.122097435464422, -15.138617059421884), (16.181113232566613, -14.28061816309008), (15.459304637239855, -14.748204863207413), (15.12790823812757, -14.552998765100176), (15.18692403522976, -13.694999868768372), (14.465115439903002, -14.162586568885704), (14.13371904079072, -13.967380470778467), (14.192734837892907, -13.109381574446664), (11.935214723555426, -11.071342582336431), (13.409721104541616, -13.731385990333942), (13.353802583701809, -13.775806114031365), (13.82138928381914, -14.497614709358121), (13.626183185711904, -14.829011108470405), (12.7681842893801, -14.769995311368216), (13.235770989497432, -15.491803906694974), (13.040564891390195, -15.823200305807259), (12.182565995058392, -15.76418450870507), (12.650152695175723, -16.485993104031827), (12.454946597068487, -16.81738950314411), (11.596947700736681, -16.758373706041922), (11.774253507822554, -17.599924430114946), (11.47309437961052, -17.8391568977639), (10.693470316100578, -17.476071108988783), (10.87077612318645, -18.317621833061807), (10.569616994974417, -18.55685430071076), (9.789992931464475, -18.193768511935644), (9.967298738550348, -19.035319236008668), (9.666139610338314, -19.27455170365762), (8.886515546828372, -18.911465914882506), (5.070079546182985, -20.10930407297309), (5.369539085705631, -21.063413073134438), (7.067752577894353, -21.336636089377556), (7.298106069834851, -22.070566089501668), (6.0605995615271215, -23.265203073506775), (7.758813053715846, -23.538426089749894), (7.989166545656343, -24.272356089874005), (6.751660037348612, -25.466993073879117), (8.449873529537339, -25.74021609012223), (8.680227021477837, -26.474146090246343), (7.442720513170102, -27.668783074251454), (9.581292005433298, -27.80379399533027), (7.277757086028323, -20.464493994089146), (9.185975086351018, -19.86557491504385), (9.207360834503616, -19.93371211588275), (12.21895211662396, -17.541387439393212), (12.263372240321386, -17.597305960233022), (14.215433221393747, -14.283341969110179), (15.077063859085685, -14.790877824188993), (15.544650559203017, -15.512686419515749), (15.34944446109578, -15.844082818628033), (14.491445564763977, -15.785067021525844), (14.959032264881309, -16.5068756168526), (14.763826166774072, -16.838272015964886), (13.905827270442268, -16.7792562188627), (14.3734139705596, -17.501064814189455), (14.178207872452363, -17.832461213301738), (13.320208976120558, -17.77344541619955), (13.986633515705263, -18.61237767039065), (15.938694496777623, -15.298413679267806), (16.667766574824654, -15.72786709510373), (15.575974328434185, -18.566526935718954), (17.529397212516596, -16.235402950182543), (20.57461234298948, -11.06561912403091), (15.404828516837844, -8.020403993558027), (21.082148198068293, -10.20398848633897), (15.912364371916658, -7.158773355866088), (17.47697688873649, -4.502570711032417), (18.553914126663095, -1.7025338924232385), (17.620568520460036, -1.3435548131143693), (16.9026103618423, -3.2102460255204885), (14.10257354323312, -2.133308787593881), (14.538461538461537, -1), (14.209663563850821, 0.9727878476642875), (19.963628119538328, 2.945575695328576), (13.880865589240106, 2.945575695328575), (13.538461538461537, 5), (12.538461538461537, -1), (12.038461538461537, -0.49999999999999967), (12.038461538461537, 1), (12.538461538461537, 1.5000000000000002), (11.538461538461537, 7.5), (11.538461538461537, -1), (3, -1), (3, 3), (0, 3), (0, -15), (3, -15), (3, -4), (4.153846153846155, -1.6923076923076925), (4.923076923076924, -2.0769230769230775), (4.923076923076924, -2.4615384615384617), (4.153846153846155, -2.8461538461538463), (4.923076923076924, -3.230769230769231), (4.923076923076923, -3.6153846153846154), (4.153846153846155, -4), (4.923076923076924, -4.384615384615385), (4.923076923076924, -4.769230769230769), (4.153846153846154, -5.153846153846153), (5.153846153846157, -5.538461538461538), (5.153846153846155, -1.6923076923076925), (5.307692307692308, -1.692307692307693), (6.461538461538462, -4), (7.149559377692243, -3.483984312884664), (7.493569835769134, -3.6559895419231094), (7.493569835769134, -4.5160156871153365), (8.181590751922915, -4), (8.525601209999806, -4.1720052290384455), (8.525601209999806, -5.032031374230673), (9.213622126153588, -4.5160156871153365), (9.557632584230477, -4.688020916153782), (9.557632584230477, -5.54804706134601), (10.344134055268762, -6.165635464778759), (11.81400257625926, -9.275909738476889), (8.667996692106117, -6.805556124745889), (5.999698077274886, -5.346041649966782), (4.522727089418631, -6.694580378009444), (5.196996453439962, -7.433065871937571), (6.673967441296217, -6.08452714389491), (4.795645641522501, -8.476577982922965), (7.348236805317548, -6.8230126378230365), (3.655809335676912, -10.194359457929691), (4.330078699698245, -10.93284495185782), (8.022506169338879, -7.561498131751164), (8.050408288673367, -7.592057595784175), (11.19641417282651, -10.062411209515174), (10.863866570978105, -10.485912001612713), (7.4937260394253045, -9.795642254186232), (8.963594560415801, -12.905916527884361), (8.261549623180283, -12.99037306168713), (7.081797416622855, -12.063990456538004), (6.997340882820088, -11.361945519302488), (6.379752479387339, -12.148446990340773), (8.346006156983051, -13.692417998922647), (8.013458555134648, -14.115918791020185), (6.05413409134202, -13.714611370725308), (5.377722263016946, -13.18346919680562), (5.454896766919807, -12.806676030691651), (6.285657603050603, -12.584231872383407), (5.6092457747255295, -12.053089698463719), (5.686420278628391, -11.67629653234975), (6.517181114759186, -11.453852374041507), (5.840769286434113, -10.922710200121816), (5.917943790336974, -10.54591703400785), (6.748704626467768, -10.323472875699604), (5.846216898474315, -9.7460259994382), (5.074471859445706, -13.51395766057787), (4.6433180235818465, -13.425649043593705), (6.1131865445723435, -16.535923317291836), (5.163050539291191, -17.74592558042766), (4.183388307394877, -17.54527187028022), (3.5069764790698046, -17.01412969636053), (3.5841509829726657, -16.637336530246564), (4.414911819103461, -16.41489237193832), (3.7384999907783873, -15.883750198018632), (3.815674494681248, -15.506957031904664), (4.646435330812044, -15.28451287359642), (3.97002350248697, -14.75337069967673), (4.047198006389832, -14.376577533562763), (4.877958842520626, -14.154133375254517), (3.9754711145271724, -13.576686498993112), (3.2037260754985635, -17.344618160132782), (3.315856089992722, -14.30530460937012), (2.597897931374982, -16.17199582177624), (-1.1354844934372554, -14.736079504540761), (-0.05854725551064721, -11.936042685931582), (-0.991892861713707, -11.577063606622714), (-2.068830099640315, -14.377100425231891), (-3.9355213120464336, -13.659142266614152), (-4.222704575493529, -13.012979923858188), (-3.6842359565302245, -11.612961514553598), (-3.03807361377426, -11.325778251106504), (-2.3201154551565204, -9.459087038700385), (-3.25346106135958, -9.100107959391515), (-5.2278459975583615, -14.233508793508342), (2.2389188520661123, -17.105341427979297), (2.2240638436022495, -17.143964449985344), (1.7929100077383886, -17.05565583300118), (2.305286383548092, -17.914416829735494), (1.9788351034429243, -18.71007663903335)

#for p in range(0,360):
	#xs.append((360*math.cos(0.0174533*p),360 + 360*math.sin(0.0174533*p)))

x = []
y=[]


for q in range(0,2):
    if q==0:
        toAdd = x
    else:
        toAdd = y
    for h in xs:
        toAdd.append(h[q])

print x, " ", y
x.append(xs[0][0])
y.append(xs[0][1])
#x+=[2,4]
#y+=[2,4]

#plt.figure(1)
#plt.subplot(211)
plt.plot(x, y)
xs = (13.32938783395248, -4.143591631723548), (-6.28383761542234, -15.757055793279832), (6.748704626467768, -10.323472875699604), (-3.3948861842989673, 0.576618237624652), (-3.6842359565302245, -11.612961514553598), (-8.848308613966006, -13.801525803307438), (5.377722263016946, -13.18346919680562), (12.86978177498105, -10.050590381571837), (-3.209970254102751, -18.352658060880984), (14.368874293859438, -12.052544838647485), (-6.5461907149045055, -13.039742565621609), (-2.1052563093935546, -18.685776729091888), (-9.220254560275531, -3.3399660915269482), (-8.874988654447641, -1.3701706485931195), (-8.74455843314456, -2.3616281400524506), (8.525601209999806, -4.1720052290384455), (15.575974328434185, -18.566526935718954), (-7.195334889012972, -15.049571753189595), (-2.7138551901956456, -11.54846741331332), (9.557632584230477, -4.688020916153782), (11.774253507822554, -17.599924430114946), (14.3734139705596, -17.501064814189455), (11.538461538461537, -1), (-9.877930231945196, -11.464663781333917), (-6.394289191173172, -9.160448704154694), (13.29625130355474, -7.0154242661945005), (-19.494356497833486, -6.24925381315709), (13.82138928381914, -14.497614709358121), (2.6260948895867244, 5.493059427164913), (-22.034397563886895, -7.11125374284497), (-9.445078620000578, -12.813990230964315), (-10.080418284446848, -10.328723846592801), (-7.199100793177457, 0.6347738003408527), (0.0039613051070399585, -18.085725528640516), (14.89729266175903, -8.882034631249967), (2.305286383548092, -17.914416829735494), (-4.606234469899106, -8.623729583644497), (-8.949074633872854, 5.6803958250324955), (-9.135849097053804, 0.6127443343255422), (15.207806548050538, -11.386120299062782), (-8.251538607931435, -14.78906137565056), (12.650152695175723, -16.485993104031827), (13.235770989497432, -15.491803906694974), (-1.435404079896271, -19.12879863017433), (-5.2278459975583615, -14.233508793508342), (15.912364371916658, -7.158773355866088), (14.341734262286593, -9.304690660893437), (6.90875205703842, -3.1055728090000843), (-1.1467012341134861, -18.171379878093028), (9.967298738550348, -19.035319236008668), (7.277757086028323, -20.464493994089146), (9.207360834503616, -19.93371211588275), (-9.024261986309105, -5.7335700756227), (-6.314008544438785, 0.9839688103420045), (16.9026103618423, -3.2102460255204885), (6.461538461538462, -4), (-10.645086358897823, -8.475988232524603), (4.872091443232934, 13.779693991456465), (-4.314684198811948, -18.019539392670076), (5.840769286434113, -10.922710200121816), (5.6092457747255295, -12.053089698463719), (13.320208976120558, -17.77344541619955), (-23.678381921649372, -4.92918659296849), (3.8597198357787352, 3.099699969805287), (-1.1228377840397241, 11.036534284999359), (-7.424741487537748, -13.517391537048884), (0, -15), (8.680227021477837, -26.474146090246343), (6.1131865445723435, -16.535923317291836), (-16.42717245359818, -6.585545498989408), (-2.10295873681365, -10.569607632756952), (-3.4733209482398064, -8.842516921457008), (1.3158124903571917, 3.982046510519487), (-10.2829063369485, -9.192783911851684), (-18.34119083443781, -6.2888757705895335), (12.915181203980708, -5.220528869650154), (9.923076923076923, -4), (-16.35849439404861, -4.58672501577024), (3.5069764790698046, -17.01412969636053), (-9.0767761860275, -8.642408997592376), (15.544650559203017, -15.512686419515749), (-8.843273192017886, -4.43049165048105), (-8.051199051710345, -15.566772425086222), (7.081797416622855, -12.063990456538004), (-4.702595870998052, 6.908370225831227), (5.196996453439962, -7.433065871937571), (3.7384999907783873, -15.883750198018632), (-2.191125325878914, -22.38867298354031), (13.880865589240106, 2.945575695328575), (-17.18802517104214, -6.328497728021977), (-5.739147991558405, -8.404942245831984), (14.959032264881309, -16.5068756168526), (11.935214723555426, -11.071342582336431), (-9.815341040323997, -2.324836806224376), (16.453493834576708, -15.333823157529121), (14.538461538461537, -1), (-20.57584660726516, -3.676019786152447), (1.154623844327566, -18.000071179188005), (-5.794250937348989, -1.1976447733819453), (8.886515546828372, -18.911465914882506), (7.989166545656343, -24.272356089874005), (-0.1283823696949531, -5.229238548415534), (17.468565544734336, -13.610561882145243), (8.346006156983051, -13.692417998922647), (-8.618863916105935, -11.321014605465779), (10.863866570978105, -10.485912001612713), (-11.9963921582322, -3.078799542739664), (-6.055111379955151, 0.7852702095367154), (11.076923076923077, -4.192307692307692), (-0.991892861713707, -11.577063606622714), (-8.46629182376024, -5.5210172094351515), (-1.2798900501028136, -1.4166009543205296), (-1.8109638336494447, -8.212959116120668), (14.465115439903002, -14.162586568885704), (-14.177443276140405, -3.8327622792549523), (-10.294107067894963, -10.444950786075871), (-1.4920622834316548, -9.590747852200584), (15.459304637239855, -14.748204863207413), (-4.718729049570742, -7.583527908123098), (7.298106069834851, -22.070566089501668), (-2.680038651556118, -13.383057380319542), (3, 3), (3.315856089992722, -14.30530460937012), (1.7723869667409986, -20.023858941341675), (13.743594463924252, -3.0666543937969406), (11.81400257625926, -9.275909738476889), (4.877958842520626, -14.154133375254517), (5.369539085705631, -21.063413073134438), (8.050408288673367, -7.592057595784175), (-9.945787780933875, -3.3162921243624446), (-0.20936917956895718, -21.20626596244099), (-8.082229763793599, -1.4986375917736718), (-5.372340341831708, -16.464539833370072), (15.480187150060631, -12.439325293501822), (3, -4), (5.618031499322387, 0.16056449905732562), (3.97002350248697, -14.75337069967673), (3.3300391351674996, -19.631938823204123), (6.40106570217418, 1.4399617935535494), (7.348236805317548, -6.8230126378230365), (10.87077612318645, -18.317621833061807), (7.493569835769134, -3.6559895419231094), (-6.938240350571295, -1.3481411825778085), (-22.48887236108464, -3.4069783900954476), (12.038461538461537, 1), (-8.343090206399761, 0.4842773911449897), (16.474376347397484, -13.024943587823532), (12.263372240321386, -17.597305960233022), (11.576923076923077, -2.192307692307692), (-5.876249484610855, -6.477961709300366), (4.153846153846154, -5.153846153846153), (4.153846153846155, -4), (4.153846153846155, -2.8461538461538463), (4.153846153846155, -1.6923076923076925)
x=[]
y=[]
for q in range(0,2):
    if q==0:
        toAdd = x
    else:
        toAdd = y
    for h in xs:
        toAdd.append(h[q])
plt.plot(x,y,'ro')
#plt.axis([-10, 30, 60, 40])
plt.show()
#print intersection((2,-3),(7,28))

#print intersection ((equation(3,2.5,3,2)),(equation(3,2.5,3,3)))

#(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (3, 2), (3, 3), (0, 3); (2, 0), (3, 2.5)

