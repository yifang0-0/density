import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import json
def create_kind(name,path1,path2,max_edges=41172):
    g = nx.Graph()
    #max_edges = 41172
    genre_test=name
    with open(path2,'r',encoding='utf-8') as file:
        genre=json.load(file)
    with open(path1) as f:
        for line in f:
            max_edges -= 1

            if max_edges <= 0:
                break

            n0, n1 = line.split(',')
                    #n0=n0.rstrip('\n')
            n1=n1.rstrip('\n')

            genre_n0=genre[n0]
            genre_n1=genre[n1]
            feature0=[]
            feature1=[]
            for ft in genre_n0:
                feature0.append(ft/10)
            for ft in genre_n1:
                feature1.append(ft/10)
            if genre_test in feature0 and genre_test in feature1:
                g.add_nodes_from([n0, n1])
                g.add_edge(n0, n1)/
            elif genre_test in feature0:
                g.add_node(n0)
            elif genre_test in feature1:
                g.add_node(n1)
    return g
def create(name,path1,path2,max_edges=41172):
    g = nx.Graph()
    #max_edges = 41172
    genre_test=name
    with open(path2,'r',encoding='utf-8') as file:
        genre=json.load(file)
    with open(path1) as f:
        for line in f:
            max_edges -= 1

            if max_edges <= 0:
                break

            n0, n1 = line.split(',')
                    #n0=n0.rstrip('\n')
            n1=n1.rstrip('\n')
            if n0=="node_1":
                continue
            genre_n0=genre[n0]
            genre_n1=genre[n1]

            if genre_test in genre_n0 and genre_test in genre_n1:
                g.add_nodes_from([n0, n1])
                g.add_edge(n0, n1)
            elif genre_test in genre_n0:
                g.add_node(n0)
            elif genre_test in genre_n1:
                g.add_node(n1)
    return g


def create_random():
    return nx.generators.watts_strogatz_graph(1000, 6, 0.3)


# 计算网络直径
def calc_diameter(g):
    path_len = nx.all_pairs_shortest_path_length(g)
    max_len = 0
    for start, ends in path_len:
        for end, len_ in ends.items():
            if len_ > max_len:
                max_len = len_
    return max_len


def degree_histogram(g):
    hist = nx.degree_histogram(g)
    # 度总数
    sum_count = sum(hist)
    # x轴为度数
    x = range(len(hist))
    # y轴为频率
    y = [n / sum_count for n in hist]
    # plt.plot(x, y)
    plt.loglog(x, y)
    plt.show()

def networkDensity(g,name,f,x,y):
    edges=g.number_of_edges()
    n=g.number_of_nodes()
    if n>1:
        density=edges*2/(n*(n-1))
    else:
        density=0
    if density!=0:
        x.append(n)
        y.append(density)
    out=repr(n)+','+repr(density)+','+name+'\n'
    f.write(out)
   # f.write(n,",",density)
    print("n=",n)
    print("name:",name)
    print("density=",density,'\n')


def draw(g,name):
    plt.rcParams['figure.figsize'] = (19.8, 12.8)
    print("drawing")
    nx.draw_spring(g, node_size=30,alpha=0.5, cmap=plt.get_cmap('jet'))
    print("drew")
    plt.savefig("./Pop.png")


def xyList(x,y,path1,path2,feature,nodenum=41172):
     with open("test.txt", "a", encoding="utf8") as f:
        f.write("n , density")
        for name in feature:
            g = create(name,path1,path2,nodenum)
       # degree_histogram(g)
            networkDensity(g,name,f,x,y)
       # print(calc_diameter(g))

def drawMusic():
    genre=['Films/Games', 'African Music', 'Tropical', 'Baroque', 'Stories', 'TV shows & movies', 'International Pop', 'Contemporary Soul', 'Chill Out/Trip-Hop/Lounge', 'Country Blues', 'Pop', 'Old school soul', 'Dancefloor', 'West Coast', 'Grime', 'Indie Pop/Folk', 'Hard Rock', 'Alternative Country', 'Acoustic Blues', 'Vocal jazz', 'Kids', 'Country', 'Rock', 'Alternative', 'Old School', 'Blues', 'Latin Music', 'Dance', 'Bolero', 'Dancehall/Ragga', 'Indie Pop', 'Modern', 'Folk', 'Rock & Roll/Rockabilly', 'Musicals', 'Disco', 'Indian Music', 'Rap/Hip Hop', 'Oldschool R&B', 'Trance', 'Electro', 'Ranchera', 'Classical Period', 'Nursery Rhymes', 'Game Scores', 'Jazz', 'Dirty South', 'Soul & Funk', 'Kids & Family', 'Electro Pop/Electro Rock', 'Bollywood', 'Film Scores', 'R&B', 'Comedy', 'Bluegrass', 'Contemporary R&B', 'Electro Hip Hop', 'Soundtracks', 'Asian Music', 'Instrumental jazz', 'Spirituality & Religion', 'Dub', 'Indie Rock', 'Ska', 'Romantic', 'Classic Blues', 'Indie Rock/Rock pop', 'Reggae', 'East Coast', 'Opera', 'Jazz Hip Hop', 'Urban Cowboy', 'Brazilian Music', 'Sports', 'Dubstep', 'Techno/House', 'Corridos', 'Classical', 'TV Soundtracks', 'Chicago Blues', 'Electric Blues', 'Norteño', 'Metal', 'Singer & Songwriter']
    x1=[]
    y1=[]
    x2=[]
    y2=[]
    x3=[]
    y3=[]
    path1=['./data/deezer_clean_data/RO_edges.csv','./data/deezer_clean_data/HU_edges.csv','./data/deezer_clean_data/HR_edges.csv']
    path2=['./data/deezer_clean_data/RO_genres.json','./data/deezer_clean_data/HU_genres.json','./data/deezer_clean_data/HR_genres.json']
    print("RO")
    xyList(x1,y1,path1[0],path2[0],genre)
    print("HU")
    xyList(x2,y2,path1[1],path2[1],genre)
    print("HR")
    xyList(x3,y3,path1[2],path2[2],genre)
    fig = plt.figure(0)
    plt.xlabel('nodeNum_sqrt')
    plt.ylabel('density')
    #plt.ylim(0.00010,0.0005)
    plt.title('NODE & DENSITY of Music Genre')
    plt.scatter(np.log10(x1),np.log10(y1), c='red', alpha=1, marker='+', label='RO')
    plt.scatter(np.log10(x2),np.log10(y2), c='blue', alpha=1, marker='>', label='RU')
    plt.scatter(np.log10(x3),np.log10(y3), c='green', alpha=1, marker='*', label='HU')

    plt.grid(True)
    plt.legend(loc='best')
    plt.show()

def drawFacebook():
    #分别读入四个属性
    path1=["./data/facebook_large/facebook_large/musae_facebook_edges.csv"]
    path2=["./data/facebook_large/facebook_large/musae_facebook_features.json"]
    x1=[]
    y1=[]#feature
    feature=[]
    for i in range(470):
        feature.append(i)
    xyList(x1,y1,path1[0],path2[0],feature,22425)
    plt.xlabel('nodeNum')
    plt.ylabel('density')
    #plt.ylim(0.00010,0.0005)
    plt.title('NODE & DENSITY of Facebook feature')
    plt.scatter(np.log10(x1),np.log10(y1), c='red', alpha=1, marker='+',label='RO')
    plt.scatter(np.log10(x2),np.log10(y2), c='blue', alpha=1, marker='>', label='RU')
    plt.scatter(np.log10(x3),np.log10(y3), c='green', alpha=1, marker='*', label='HU')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
   #drawFacebook()
   drawMusic()