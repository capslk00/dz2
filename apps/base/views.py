from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('Hello world')

def index(request):
    return render(request, 'index.html')

def about(request):
    text = {
        'title': 'Все обо мне',
        'description': 'Я ученик 19-1В',
        'loremipsum': 'Lorem ipsum odor amet, consectetuer adipiscing elit. Montes id integer nunc eleifend; congue sollicitudin morbi. Dignissim leo parturient tortor placerat porttitor platea mollis in. Curae nunc tortor viverra morbi nisi convallis ornare. Integer gravida sociosqu, nam habitasse suscipit nulla justo. Praesent erat ullamcorper molestie nibh bibendum. Morbi aenean lacinia rhoncus imperdiet morbi scelerisque. Tortor proin fermentum venenatis ipsum praesent, ornare sollicitudin mattis. Odio vivamus sapien laoreet fringilla justo nisl vitae pellentesque montes? Cursus nisl tristique justo mus odio lobortis vulputate curabitur euismod. Eget parturient dictumst at rhoncus litora. Magna aliquam interdum efficitur viverra ante. Lectus quam id nascetur etiam non. Vulputate maecenas ipsum finibus torquent phasellus eu taciti. Vestibulum metus sagittis vehicula ornare; montes magna. Accumsan erat fusce ante neque penatibus pellentesque. Etiam vel rutrum torquent proin molestie ac. Hac malesuada vel torquent sapien sapien ipsum. Libero suspendisse suspendisse est torquent pretium in. Aliquam finibus finibus bibendum aliquet justo; nec faucibus. Accumsan habitant fringilla nisl pharetra cursus morbi ut. Fermentum mus non vel ornare placerat himenaeos at. Quam mauris ligula class libero etiam odio leo dis integer. Magnis felis sociosqu lacus egestas per mauris cras curabitur. Suspendisse laoreet duis sit lobortis hendrerit. Leo pulvinar duis, cubilia commodo senectus dis ad. Vehicula primis sem purus inceptos inceptos dignissim at inceptos varius. Fusce dui ante tristique; scelerisque porta vel metus senectus. Eu velit justo cubilia ipsum phasellus cursus lectus proin. Sodales ac orci aptent primis tellus egestas. Fames eleifend ante at cursus maximus? Velit diam ex viverra urna ullamcorper class. Potenti augue pretium pretium senectus maximus nam. Facilisis dis cursus diam nam cubilia commodo. Torquent elit justo accumsan dolor eros nibh placerat. Scelerisque varius dignissim ultrices leo nisi dui eu? Nisl litora quis ultricies pulvinar potenti maecenas cubilia consequat. Purus fringilla at eros felis lacus praesent commodo nullam. Malesuada cras fames turpis malesuada iaculis porttitor arcu. In odio iaculis gravida hendrerit varius enim ultricies. Est tempus ad dignissim porttitor at hendrerit ante. Facilisis a adipiscing fames, leo amet ridiculus. Efficitur convallis purus convallis feugiat sed nulla. Laoreet magnis semper hendrerit nec dolor morbi. Proin penatibus massa nulla nec quis fermentum. Elit ornare quam tortor ex curae bibendum platea. Suspendisse convallis mi arcu habitant ullamcorper phasellus varius. Nunc sapien nunc tincidunt donec sollicitudin litora sodales tortor. Gravida odio class tempor, metus vestibulum taciti mus ac facilisis. Ut nulla id lacus dolor velit sed. Turpis per semper malesuada pharetra, vivamus mi mus. Volutpat ultrices nec neque torquent cubilia per scelerisque. Convallis nascetur libero cubilia tincidunt finibus mollis integer metus proin. Ultrices magna cras montes imperdiet libero dignissim ipsum fermentum. Leo arcu tincidunt, etiam porta rhoncus taciti. Iaculis accumsan nulla leo commodo est ornare dictum platea velit. Facilisi pharetra lobortis dapibus hac donec eu aliquam auctor. Eros auctor diam orci et proin ultrices! Vivamus ad ut luctus finibus libero quis. Imperdiet etiam bibendum ad lacus varius. Fames ad commodo risus sed et, tellus aliquam ornare finibus. Vehicula odio ultrices mus, facilisis accumsan fermentum. Aptent facilisi nostra, risus tortor nisi eleifend? Et platea sit tempus senectus porta sit sodales vulputate finibus. Per ex torquent vulputate velit primis proin. Tristique urna praesent vivamus facilisis odio accumsan egestas lectus. Libero pellentesque etiam velit himenaeos; maximus leo mus. Gravida integer facilisis non elementum nam quis senectus est conubia. Senectus nec vulputate posuere amet leo ipsum ex convallis. Quis netus nulla ultricies sagittis vel lobortis semper. Lectus leo habitant magnis purus; volutpat ultricies placerat. Auctor fusce blandit mattis aliquam sagittis. Nullam fermentum accumsan ridiculus lobortis senectus sed maecenas. Enim commodo netus et; lorem placerat suscipit. At amet montes commodo feugiat inceptos ligula volutpat. Luctus sem egestas porta; vehicula ullamcorper ridiculus tristique fringilla. Ipsum primis quis aenean augue etiam magna euismod elit. Conubia phasellus hac magnis duis ex. Lectus morbi erat cras pharetra vel est. Risus quam venenatis nisl hac euismod eleifend? Lobortis urna nunc purus tortor taciti. Montes curabitur vulputate primis nascetur porttitor curae vel. Per fames sagittis; facilisis etiam malesuada integer. Faucibus non fermentum turpis curae curabitur metus mus vehicula. Eleifend semper vel massa sociosqu enim. Ullamcorper faucibus nisl litora sagittis, malesuada fames dolor. Nunc elit adipiscing mi feugiat convallis fames vel per. Nulla dictum risus tristique aliquam amet pharetra ex vel in. Orci scelerisque cras porta a porttitor. Velit semper aenean erat finibus ridiculus sagittis dolor ligula pulvinar. Morbi nec volutpat nam eu eget orci mus. Urna montes eleifend consectetur facilisi nisi rutrum nam sodales. Dolor justo tempor diam, nostra felis sodales. Nostra placerat egestas ad lectus cras tristique eleifend ex congue? Augue suscipit fringilla neque mauris maximus sociosqu fusce magnis. Maximus mattis quis praesent eget sem eros amet a. Et risus lacus nisi pulvinar fermentum varius fermentum integer. Torquent nisl dui proin finibus at blandit mollis rhoncus eu? Dapibus tellus convallis sodales maecenas hendrerit torquent. Tellus euismod fermentum bibendum accumsan odio. Aliquet eros rhoncus curae pulvinar in posuere pellentesque. Class elit scelerisque et platea vulputate rutrum. Posuere auctor tempus a pretium elit praesent nibh at primis. Mi ornare natoque convallis volutpat ante faucibus molestie. Feugiat et ligula nec malesuada quis aenean odio potenti ridiculus. Platea fermentum eget mauris aptent eros elementum. Vivamus dui sit ad erat facilisis vestibulum. Velit augue platea cursus penatibus mollis. Praesent nibh amet morbi accumsan, magnis urna ante natoque vel. Aptent montes nisi urna lectus quisque imperdiet nascetur; sodales ultricies. Facilisi placerat natoque nam ligula sollicitudin enim nascetur fames. Egestas massa efficitur cubilia, congue parturient vivamus venenatis proin curae. Vehicula laoreet mattis varius himenaeos donec nostra euismod vel. Commodo viverra ut; aenean sit efficitur mattis inceptos. Aenean interdum curabitur mus lacus curabitur platea. Varius conubia leo et vulputate penatibus massa. Urna proin tempor vitae facilisis sapien arcu. Hendrerit penatibus at enim facilisis in sagittis nascetur. Montes magnis nam adipiscing arcu viverra vehicula in platea. Nostra mi eleifend euismod dapibus praesent commodo. Nostra interdum augue in turpis vestibulum semper lacus mauris ut. Consectetur quis netus, purus praesent maecenas aptent sodales. Nostra dictum viverra quam in, elementum penatibus eleifend placerat egestas. Amet luctus nullam himenaeos ultrices tempor litora. Pharetra dui fames ultrices dictum conubia proin maximus duis. Tristique pretium massa cursus integer gravida felis, laoreet hac. Montes dolor litora metus nascetur odio. Tempor mauris volutpat parturient luctus habitant adipiscing accumsan. Consectetur taciti et tellus dis tristique per ultricies laoreet. Accumsan platea rutrum a arcu facilisis curae dis primis. Cubilia suscipit molestie nunc eu metus morbi per duis. Conubia risus porta mattis conubia sit nostra mi ipsum. Felis diam cursus elit rhoncus ad. Montes curabitur felis tellus at pharetra enim porta. Sagittis dapibus semper montes vivamus feugiat parturient praesent nulla. Habitasse enim per orci sed per! Urna phasellus orci gravida amet a. Fames elit fringilla augue turpis auctor condimentum mus consequat rhoncus. Magna eros conubia primis id massa nisl donec accumsan euismod. Tempor magnis mi sociosqu orci diam. Hac leo lacinia consectetur accumsan metus gravida. Placerat eu tellus mus suscipit aenean. Commodo dignissim curae nullam velit lobortis elementum himenaeos; nam imperdiet. Fermentum eleifend ad phasellus elementum porta feugiat id elementum? Elementum potenti et nulla eros tempor potenti ipsum. Nec scelerisque libero egestas dis leo mauris laoreet. Habitant proin torquent phasellus fames commodo in. Tristique tortor arcu torquent vehicula fames per. Facilisi fringilla aliquam maximus imperdiet quam! Sollicitudin vivamus curae consequat eleifend mattis platea. Nisi felis condimentum lacinia aptent id at faucibus pharetra accumsan. Aliquet condimentum nascetur felis; malesuada magnis natoque maecenas. Aptent egestas hac fames mollis mauris augue ante tincidunt dignissim. Vulputate aliquet congue adipiscing pharetra velit magnis habitant etiam. At imperdiet urna tempus etiam, nisi odio ornare molestie senectus. Aptent fusce metus class; mauris velit velit nibh. Gravida libero magnis lacus dapibus massa molestie eu mollis. Ridiculus sem congue nibh lacinia odio congue. Neque vel phasellus montes maecenas, sem lectus euismod. Dis sem dis eleifend feugiat erat nulla, pellentesque sagittis. Eleifend sodales scelerisque purus adipiscing primis curabitur montes per nulla. Condimentum donec et orci penatibus vehicula molestie. Tellus varius integer natoque sed porttitor taciti dui. Pulvinar luctus nisi dolor etiam ligula quis mus. Luctus volutpat aptent morbi varius, risus natoque. Semper integer in orci suscipit orci massa ipsum facilisis. Dapibus molestie egestas rutrum adipiscing magna tellus ultrices. Maximus eget scelerisque tellus hendrerit ad. Neque habitant lobortis suspendisse ultrices velit habitasse inceptos. Leo ornare urna penatibus vitae gravida facilisis. Ridiculus magna bibendum taciti cras sollicitudin ex ligula. Sociosqu massa sem nulla justo lacinia aliquam. Magna a pulvinar class sociosqu natoque felis. Lacinia conubia arcu nullam natoque magna dignissim hac quam. Risus adipiscing posuere proin bibendum per vestibulum. Ipsum suspendisse habitasse gravida morbi maecenas pretium aliquam scelerisque. Condimentum torquent amet dui mi penatibus a fermentum. Potenti dolor sagittis dui, dapibus quisque odio. Efficitur sed id auctor pellentesque platea scelerisque lectus posuere ex. Rutrum a penatibus duis vivamus mus condimentum. Commodo platea ridiculus platea quisque neque ornare et mollis. Himenaeos aliquam facilisi cubilia quisque ornare. Ipsum elit ullamcorper eros dui convallis. Duis non consectetur commodo nascetur mauris leo. Massa vulputate quisque commodo ridiculus id sem taciti potenti cursus. Sem suspendisse metus ornare morbi facilisi dui suspendisse varius. Duis congue aliquet tellus pharetra eget sollicitudin. Nec laoreet cursus mollis sapien habitasse vivamus potenti. Consectetur nostra finibus fusce cras pulvinar placerat taciti maecenas. Ultricies enim elit hendrerit est dictum. Convallis torquent malesuada velit at velit quis. Interdum pharetra volutpat ullamcorper adipiscing hendrerit. Aliquet fames montes vel risus curabitur dis. Purus leo fusce magnis neque feugiat nibh lacinia sapien auctor. Lacus vel sodales iaculis mi tellus interdum. Semper sit non dictum elementum class facilisis hac. Nascetur in libero eget; imperdiet class ridiculus. Torquent facilisi ligula volutpat, vehicula ultrices iaculis. Platea pretium suspendisse venenatis ligula sit. Sollicitudin neque curae maximus nulla ex felis. Ipsum iaculis sem nec tellus morbi. Integer tincidunt magnis mattis eleifend sapien. Purus vulputate gravida montes parturient; lacus viverra. Lacinia neque praesent class hac dignissim. Tortor semper fames odio torquent risus nam. Porttitor pharetra felis morbi ante, varius laoreet pulvinar. Platea sit vitae vel sed nam facilisi torquent nunc. Volutpat luctus dolor metus class eu. Leo natoque donec arcu justo convallis netus. Mi neque magna bibendum consequat class fringilla venenatis nisi ultrices. Conubia cras montes congue penatibus rhoncus vel fermentum arcu. Magnis per aenean porttitor porttitor orci curae dapibus et fusce. Convallis justo ultricies non porta fermentum dignissim diam. Mauris semper natoque varius adipiscing maximus pulvinar adipiscing sapien. Sollicitudin integer pretium pharetra proin ipsum vulputate proin lobortis rutrum. Facilisis nostra interdum eros duis proin platea imperdiet purus. Orci maximus faucibus sapien enim cras faucibus curabitur. Per id at maximus sollicitudin enim phasellus per integer. Malesuada hac suscipit metus vehicula leo. Euismod amet consequat pellentesque tellus fermentum enim scelerisque dis? Vivamus egestas habitasse ridiculus leo amet. Lacus est massa facilisi hendrerit efficitur ex proin senectus. Pharetra interdum tempus dui inceptos ac; elit platea a. Ante efficitur fames lorem congue luctus primis aenean vivamus. Faucibus dictumst nisi augue vehicula libero tristique fames tristique? Turpis malesuada turpis interdum hac nascetur nisl mattis velit. Bibendum magnis imperdiet fusce primis posuere aliquam facilisis eu. Consectetur hac sociosqu et vitae nisi ligula. Ut morbi curae pharetra tincidunt pharetra quam dapibus nisl. Vitae sapien bibendum aenean nisl dignissim risus lacus cursus imperdiet. Phasellus egestas proin urna vel etiam mattis amet placerat. Neque pulvinar maximus augue iaculis potenti. Ligula dui vivamus sagittis risus, et dapibus. Mollis proin facilisis donec fringilla fames nisl ante adipiscing. Fusce aptent ac tempor habitasse sollicitudin dignissim pharetra eu. Vel mus sapien pulvinar nostra sodales mi platea mus. Laoreet imperdiet diam augue mattis mollis neque vulputate. Consectetur quis habitant purus; potenti turpis lacus. Nullam auctor et neque facilisi sollicitudin ipsum diam molestie ipsum. Maecenas per maecenas magna efficitur; integer faucibus faucibus. Accumsan nibh platea ultrices class per lobortis torquent. Aptent elementum ante sociosqu sodales eleifend potenti. Mollis lacus himenaeos non lectus, ac pretium proin amet. Odio velit netus iaculis vel curabitur litora. Tincidunt dignissim eros ac orci nascetur hendrerit aptent. Mi placerat natoque sem consectetur vulputate massa vestibulum.',
        'loading': 'Загрузка',
        'about': 'Эта страница еще дорабатывется'

    }
    return render(request, 'about.html', text)

def index(request):
    text = {
        'title': 'Все обо мне',
        'description': 'Я ученик 19-1В',
        'loremipsum': 'Lorem ipsum odor amet, consectetuer adipiscing elit. Montes id integer nunc eleifend; congue sollicitudin morbi. Dignissim leo parturient tortor placerat porttitor platea mollis in. Curae nunc tortor viverra morbi nisi convallis ornare. Integer gravida sociosqu, nam habitasse suscipit nulla justo. Praesent erat ullamcorper molestie nibh bibendum. Morbi aenean lacinia rhoncus imperdiet morbi scelerisque. Tortor proin fermentum venenatis ipsum praesent, ornare sollicitudin mattis. Odio vivamus sapien laoreet fringilla justo nisl vitae pellentesque montes? Cursus nisl tristique justo mus odio lobortis vulputate curabitur euismod. Eget parturient dictumst at rhoncus litora. Magna aliquam interdum efficitur viverra ante. Lectus quam id nascetur etiam non. Vulputate maecenas ipsum finibus torquent phasellus eu taciti. Vestibulum metus sagittis vehicula ornare; montes magna. Accumsan erat fusce ante neque penatibus pellentesque. Etiam vel rutrum torquent proin molestie ac. Hac malesuada vel torquent sapien sapien ipsum. Libero suspendisse suspendisse est torquent pretium in. Aliquam finibus finibus bibendum aliquet justo; nec faucibus. Accumsan habitant fringilla nisl pharetra cursus morbi ut. Fermentum mus non vel ornare placerat himenaeos at. Quam mauris ligula class libero etiam odio leo dis integer. Magnis felis sociosqu lacus egestas per mauris cras curabitur. Suspendisse laoreet duis sit lobortis hendrerit. Leo pulvinar duis, cubilia commodo senectus dis ad. Vehicula primis sem purus inceptos inceptos dignissim at inceptos varius. Fusce dui ante tristique; scelerisque porta vel metus senectus. Eu velit justo cubilia ipsum phasellus cursus lectus proin. Sodales ac orci aptent primis tellus egestas. Fames eleifend ante at cursus maximus? Velit diam ex viverra urna ullamcorper class. Potenti augue pretium pretium senectus maximus nam. Facilisis dis cursus diam nam cubilia commodo. Torquent elit justo accumsan dolor eros nibh placerat. Scelerisque varius dignissim ultrices leo nisi dui eu? Nisl litora quis ultricies pulvinar potenti maecenas cubilia consequat. Purus fringilla at eros felis lacus praesent commodo nullam. Malesuada cras fames turpis malesuada iaculis porttitor arcu. In odio iaculis gravida hendrerit varius enim ultricies. Est tempus ad dignissim porttitor at hendrerit ante. Facilisis a adipiscing fames, leo amet ridiculus. Efficitur convallis purus convallis feugiat sed nulla. Laoreet magnis semper hendrerit nec dolor morbi. Proin penatibus massa nulla nec quis fermentum. Elit ornare quam tortor ex curae bibendum platea. Suspendisse convallis mi arcu habitant ullamcorper phasellus varius. Nunc sapien nunc tincidunt donec sollicitudin litora sodales tortor. Gravida odio class tempor, metus vestibulum taciti mus ac facilisis. Ut nulla id lacus dolor velit sed. Turpis per semper malesuada pharetra, vivamus mi mus. Volutpat ultrices nec neque torquent cubilia per scelerisque. Convallis nascetur libero cubilia tincidunt finibus mollis integer metus proin. Ultrices magna cras montes imperdiet libero dignissim ipsum fermentum. Leo arcu tincidunt, etiam porta rhoncus taciti. Iaculis accumsan nulla leo commodo est ornare dictum platea velit. Facilisi pharetra lobortis dapibus hac donec eu aliquam auctor. Eros auctor diam orci et proin ultrices! Vivamus ad ut luctus finibus libero quis. Imperdiet etiam bibendum ad lacus varius. Fames ad commodo risus sed et, tellus aliquam ornare finibus. Vehicula odio ultrices mus, facilisis accumsan fermentum. Aptent facilisi nostra, risus tortor nisi eleifend? Et platea sit tempus senectus porta sit sodales vulputate finibus. Per ex torquent vulputate velit primis proin. Tristique urna praesent vivamus facilisis odio accumsan egestas lectus. Libero pellentesque etiam velit himenaeos; maximus leo mus. Gravida integer facilisis non elementum nam quis senectus est conubia. Senectus nec vulputate posuere amet leo ipsum ex convallis. Quis netus nulla ultricies sagittis vel lobortis semper. Lectus leo habitant magnis purus; volutpat ultricies placerat. Auctor fusce blandit mattis aliquam sagittis. Nullam fermentum accumsan ridiculus lobortis senectus sed maecenas. Enim commodo netus et; lorem placerat suscipit. At amet montes commodo feugiat inceptos ligula volutpat. Luctus sem egestas porta; vehicula ullamcorper ridiculus tristique fringilla. Ipsum primis quis aenean augue etiam magna euismod elit. Conubia phasellus hac magnis duis ex. Lectus morbi erat cras pharetra vel est. Risus quam venenatis nisl hac euismod eleifend? Lobortis urna nunc purus tortor taciti. Montes curabitur vulputate primis nascetur porttitor curae vel. Per fames sagittis; facilisis etiam malesuada integer. Faucibus non fermentum turpis curae curabitur metus mus vehicula. Eleifend semper vel massa sociosqu enim. Ullamcorper faucibus nisl litora sagittis, malesuada fames dolor. Nunc elit adipiscing mi feugiat convallis fames vel per. Nulla dictum risus tristique aliquam amet pharetra ex vel in. Orci scelerisque cras porta a porttitor. Velit semper aenean erat finibus ridiculus sagittis dolor ligula pulvinar. Morbi nec volutpat nam eu eget orci mus. Urna montes eleifend consectetur facilisi nisi rutrum nam sodales. Dolor justo tempor diam, nostra felis sodales. Nostra placerat egestas ad lectus cras tristique eleifend ex congue? Augue suscipit fringilla neque mauris maximus sociosqu fusce magnis. Maximus mattis quis praesent eget sem eros amet a. Et risus lacus nisi pulvinar fermentum varius fermentum integer. Torquent nisl dui proin finibus at blandit mollis rhoncus eu? Dapibus tellus convallis sodales maecenas hendrerit torquent. Tellus euismod fermentum bibendum accumsan odio. Aliquet eros rhoncus curae pulvinar in posuere pellentesque. Class elit scelerisque et platea vulputate rutrum. Posuere auctor tempus a pretium elit praesent nibh at primis. Mi ornare natoque convallis volutpat ante faucibus molestie. Feugiat et ligula nec malesuada quis aenean odio potenti ridiculus. Platea fermentum eget mauris aptent eros elementum. Vivamus dui sit ad erat facilisis vestibulum. Velit augue platea cursus penatibus mollis. Praesent nibh amet morbi accumsan, magnis urna ante natoque vel. Aptent montes nisi urna lectus quisque imperdiet nascetur; sodales ultricies. Facilisi placerat natoque nam ligula sollicitudin enim nascetur fames. Egestas massa efficitur cubilia, congue parturient vivamus venenatis proin curae. Vehicula laoreet mattis varius himenaeos donec nostra euismod vel. Commodo viverra ut; aenean sit efficitur mattis inceptos. Aenean interdum curabitur mus lacus curabitur platea. Varius conubia leo et vulputate penatibus massa. Urna proin tempor vitae facilisis sapien arcu. Hendrerit penatibus at enim facilisis in sagittis nascetur. Montes magnis nam adipiscing arcu viverra vehicula in platea. Nostra mi eleifend euismod dapibus praesent commodo. Nostra interdum augue in turpis vestibulum semper lacus mauris ut. Consectetur quis netus, purus praesent maecenas aptent sodales. Nostra dictum viverra quam in, elementum penatibus eleifend placerat egestas. Amet luctus nullam himenaeos ultrices tempor litora. Pharetra dui fames ultrices dictum conubia proin maximus duis. Tristique pretium massa cursus integer gravida felis, laoreet hac. Montes dolor litora metus nascetur odio. Tempor mauris volutpat parturient luctus habitant adipiscing accumsan. Consectetur taciti et tellus dis tristique per ultricies laoreet. Accumsan platea rutrum a arcu facilisis curae dis primis. Cubilia suscipit molestie nunc eu metus morbi per duis. Conubia risus porta mattis conubia sit nostra mi ipsum. Felis diam cursus elit rhoncus ad. Montes curabitur felis tellus at pharetra enim porta. Sagittis dapibus semper montes vivamus feugiat parturient praesent nulla. Habitasse enim per orci sed per! Urna phasellus orci gravida amet a. Fames elit fringilla augue turpis auctor condimentum mus consequat rhoncus. Magna eros conubia primis id massa nisl donec accumsan euismod. Tempor magnis mi sociosqu orci diam. Hac leo lacinia consectetur accumsan metus gravida. Placerat eu tellus mus suscipit aenean. Commodo dignissim curae nullam velit lobortis elementum himenaeos; nam imperdiet. Fermentum eleifend ad phasellus elementum porta feugiat id elementum? Elementum potenti et nulla eros tempor potenti ipsum. Nec scelerisque libero egestas dis leo mauris laoreet. Habitant proin torquent phasellus fames commodo in. Tristique tortor arcu torquent vehicula fames per. Facilisi fringilla aliquam maximus imperdiet quam! Sollicitudin vivamus curae consequat eleifend mattis platea. Nisi felis condimentum lacinia aptent id at faucibus pharetra accumsan. Aliquet condimentum nascetur felis; malesuada magnis natoque maecenas. Aptent egestas hac fames mollis mauris augue ante tincidunt dignissim. Vulputate aliquet congue adipiscing pharetra velit magnis habitant etiam. At imperdiet urna tempus etiam, nisi odio ornare molestie senectus. Aptent fusce metus class; mauris velit velit nibh. Gravida libero magnis lacus dapibus massa molestie eu mollis. Ridiculus sem congue nibh lacinia odio congue. Neque vel phasellus montes maecenas, sem lectus euismod. Dis sem dis eleifend feugiat erat nulla, pellentesque sagittis. Eleifend sodales scelerisque purus adipiscing primis curabitur montes per nulla. Condimentum donec et orci penatibus vehicula molestie. Tellus varius integer natoque sed porttitor taciti dui. Pulvinar luctus nisi dolor etiam ligula quis mus. Luctus volutpat aptent morbi varius, risus natoque. Semper integer in orci suscipit orci massa ipsum facilisis. Dapibus molestie egestas rutrum adipiscing magna tellus ultrices. Maximus eget scelerisque tellus hendrerit ad. Neque habitant lobortis suspendisse ultrices velit habitasse inceptos. Leo ornare urna penatibus vitae gravida facilisis. Ridiculus magna bibendum taciti cras sollicitudin ex ligula. Sociosqu massa sem nulla justo lacinia aliquam. Magna a pulvinar class sociosqu natoque felis. Lacinia conubia arcu nullam natoque magna dignissim hac quam. Risus adipiscing posuere proin bibendum per vestibulum. Ipsum suspendisse habitasse gravida morbi maecenas pretium aliquam scelerisque. Condimentum torquent amet dui mi penatibus a fermentum. Potenti dolor sagittis dui, dapibus quisque odio. Efficitur sed id auctor pellentesque platea scelerisque lectus posuere ex. Rutrum a penatibus duis vivamus mus condimentum. Commodo platea ridiculus platea quisque neque ornare et mollis. Himenaeos aliquam facilisi cubilia quisque ornare. Ipsum elit ullamcorper eros dui convallis. Duis non consectetur commodo nascetur mauris leo. Massa vulputate quisque commodo ridiculus id sem taciti potenti cursus. Sem suspendisse metus ornare morbi facilisi dui suspendisse varius. Duis congue aliquet tellus pharetra eget sollicitudin. Nec laoreet cursus mollis sapien habitasse vivamus potenti. Consectetur nostra finibus fusce cras pulvinar placerat taciti maecenas. Ultricies enim elit hendrerit est dictum. Convallis torquent malesuada velit at velit quis. Interdum pharetra volutpat ullamcorper adipiscing hendrerit. Aliquet fames montes vel risus curabitur dis. Purus leo fusce magnis neque feugiat nibh lacinia sapien auctor. Lacus vel sodales iaculis mi tellus interdum. Semper sit non dictum elementum class facilisis hac. Nascetur in libero eget; imperdiet class ridiculus. Torquent facilisi ligula volutpat, vehicula ultrices iaculis. Platea pretium suspendisse venenatis ligula sit. Sollicitudin neque curae maximus nulla ex felis. Ipsum iaculis sem nec tellus morbi. Integer tincidunt magnis mattis eleifend sapien. Purus vulputate gravida montes parturient; lacus viverra. Lacinia neque praesent class hac dignissim. Tortor semper fames odio torquent risus nam. Porttitor pharetra felis morbi ante, varius laoreet pulvinar. Platea sit vitae vel sed nam facilisi torquent nunc. Volutpat luctus dolor metus class eu. Leo natoque donec arcu justo convallis netus. Mi neque magna bibendum consequat class fringilla venenatis nisi ultrices. Conubia cras montes congue penatibus rhoncus vel fermentum arcu. Magnis per aenean porttitor porttitor orci curae dapibus et fusce. Convallis justo ultricies non porta fermentum dignissim diam. Mauris semper natoque varius adipiscing maximus pulvinar adipiscing sapien. Sollicitudin integer pretium pharetra proin ipsum vulputate proin lobortis rutrum. Facilisis nostra interdum eros duis proin platea imperdiet purus. Orci maximus faucibus sapien enim cras faucibus curabitur. Per id at maximus sollicitudin enim phasellus per integer. Malesuada hac suscipit metus vehicula leo. Euismod amet consequat pellentesque tellus fermentum enim scelerisque dis? Vivamus egestas habitasse ridiculus leo amet. Lacus est massa facilisi hendrerit efficitur ex proin senectus. Pharetra interdum tempus dui inceptos ac; elit platea a. Ante efficitur fames lorem congue luctus primis aenean vivamus. Faucibus dictumst nisi augue vehicula libero tristique fames tristique? Turpis malesuada turpis interdum hac nascetur nisl mattis velit. Bibendum magnis imperdiet fusce primis posuere aliquam facilisis eu. Consectetur hac sociosqu et vitae nisi ligula. Ut morbi curae pharetra tincidunt pharetra quam dapibus nisl. Vitae sapien bibendum aenean nisl dignissim risus lacus cursus imperdiet. Phasellus egestas proin urna vel etiam mattis amet placerat. Neque pulvinar maximus augue iaculis potenti. Ligula dui vivamus sagittis risus, et dapibus. Mollis proin facilisis donec fringilla fames nisl ante adipiscing. Fusce aptent ac tempor habitasse sollicitudin dignissim pharetra eu. Vel mus sapien pulvinar nostra sodales mi platea mus. Laoreet imperdiet diam augue mattis mollis neque vulputate. Consectetur quis habitant purus; potenti turpis lacus. Nullam auctor et neque facilisi sollicitudin ipsum diam molestie ipsum. Maecenas per maecenas magna efficitur; integer faucibus faucibus. Accumsan nibh platea ultrices class per lobortis torquent. Aptent elementum ante sociosqu sodales eleifend potenti. Mollis lacus himenaeos non lectus, ac pretium proin amet. Odio velit netus iaculis vel curabitur litora. Tincidunt dignissim eros ac orci nascetur hendrerit aptent. Mi placerat natoque sem consectetur vulputate massa vestibulum.'
    }
    return render(request, 'index.html', text)