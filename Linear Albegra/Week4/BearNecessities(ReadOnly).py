import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la

bear_black = (0.141,0.11,0.11)
bear_white = (0.89,0.856,0.856)
magenta = (0xfc/255, 0x75/255, 0xdb/255) # Brighter magenta
orange = (218/255, 171/255, 115/255)
green = (175/255, 219/255, 133/255)
white = (240/255, 245/255, 250/255)
blue1 = (70/255, 101/255, 137/255)
blue2 = (122/255, 174/255, 215/255)

def gsBasis(A) :
    B = np.array(A, dtype=np.float_)
    B[:, 0] = B[:, 0] / la.norm(B[:, 0])
    B[:, 1] = B[:, 1] - B[:, 1] @ B[:, 0] * B[:, 0]
    if la.norm(B[:, 1]) > 1e-14 :
        B[:, 1] = B[:, 1] / la.norm(B[:, 1])
    else :
        B[:, 1] = np.zeros_like(B[:,1])
    return B

def draw_mirror(bearVectors) :
    fig,ax = plt.subplots(figsize=(12, 12), dpi= 80)
    ax.set_xlim([-3.50,3.50])
    ax.set_ylim([-3.50,3.50])
    ax.set_aspect(1)
    ax.set_axis_bgcolor(blue1)
    
    gs=gsBasis(bearVectors)
    ax.plot([gs[0,0]*-5,gs[0,0]*5],[gs[1,0]*-5,gs[1,0]*5], lw=2, color=green, zorder=4)
    ax.fill([
            -5*gs[0,0],-5*gs[0,0]-5*gs[0,1], 5*gs[0,0]-5*gs[0,1],5*gs[0,0]
        ],[
            -5*gs[1,0],-5*gs[1,0]-5*gs[1,1], 5*gs[1,0]-5*gs[1,1],5*gs[1,0]
        ], color=blue2, zorder=0)
    ax.arrow(0,0,bearVectors[0,0],bearVectors[1,0], lw=3, color=orange, zorder=5, head_width=0.1)
    ax.arrow(0,0,bearVectors[0,1],bearVectors[1,1], lw=3, color=orange, zorder=5, head_width=0.1)
    ax.arrow(0,0,gs[0,0],gs[1,0], lw=3, color=magenta, zorder=6, head_width=0.1)
    ax.arrow(0,0,gs[0,1],gs[1,1], lw=3, color=magenta, zorder=6, head_width=0.1)
    return ax

bear_black_fur = np.array(
      [[ 2.0030351 ,  2.229253  ,  2.1639012 ,  2.0809546 ,  1.9728726 ,
         1.8974666 ,  1.8924396 ,  2.0030351 ,      np.nan,  2.7017972 ,
         2.8500957 ,  2.9707453 ,  3.0159889 ,  2.94561   ,  2.8299874 ,
         2.7017972 ,      np.nan,  2.1639012 ,  2.2317666 ,  2.3147132 ,
         2.299632  ,  2.2493613 ,  2.1890365 ,  2.1211711 ,  2.1337387 ,
         2.1639012 ,      np.nan,  2.4982011 ,  2.5610936 ,  2.6213642 ,
         2.633986  ,  2.5536071 ,  2.5057417 ,  2.4982011 ,      np.nan,
         2.2468478 ,  2.3247673 ,  2.4429034 ,  2.4303357 ,  2.3448755 ,
         2.2820372 ,  2.2468478 ,      np.nan,  2.1966706 ,  2.2722074 ,
         2.4055076 ,  2.481933  ,  2.449941  ,  2.4001756 ,  2.3237501 ,
         2.222442  ,  2.1984479 ,  2.1966706 ,      np.nan,  1.847196  ,
         1.7818441 ,  1.7290599 ,  1.6310321 ,  1.4575984 ,  1.3369488 ,
         1.2791375 ,  1.3671112 ,  1.8044659 ,  1.9577914 ,  2.2367936 ,
         2.5962289 ,  2.7520679 ,  2.9028799 ,  3.4005595 ,  3.3150993 ,
         3.0511783 ,  2.9531506 ,  2.8676905 ,  2.7746897 ,  2.4052003 ,
         2.2795237 ,  2.1639012 ,  1.847196  ,      np.nan,  2.0491517 ,
         2.5112591 ,  2.3175294 ,  2.1326865 ,  2.0491517 ],
       [-1.3186252 , -1.0902537 , -0.99238015, -0.96477475, -0.99488975,
        -1.1153494 , -1.2408283 , -1.3186252 ,      np.nan, -1.1881273 ,
        -1.0852346 , -1.1454645 , -1.3286636 , -1.4666904 , -1.4641808 ,
        -1.1881273 ,      np.nan, -1.5545256 , -1.5219011 , -1.4014413 ,
        -1.3512497 , -1.3412115 , -1.3989317 , -1.4917862 , -1.5419777 ,
        -1.5545256 ,      np.nan, -1.4265371 , -1.3964222 , -1.4968054 ,
        -1.6097363 , -1.64738   , -1.5545256 , -1.4265371 ,      np.nan,
        -1.6423608 , -1.6699662 , -1.677495  , -1.7176483 , -1.7477632 ,
        -1.7176483 , -1.6423608 ,      np.nan, -1.7223509 , -1.7622781 ,
        -1.7764744 , -1.7613908 , -1.8767359 , -1.9805465 , -1.9991791 ,
        -1.9672374 , -1.913114  , -1.7223509 ,      np.nan, -1.5043341 ,
        -1.5444873 , -1.486767  , -1.1504836 , -1.0626484 , -1.11284   ,
        -1.2558858 , -1.7452537 , -2.3902152 , -2.4378972 , -2.3575907 ,
        -2.1467861 , -2.2446597 , -2.5527822 , -2.5527822 , -2.1919586 ,
        -1.7828973 , -1.6850238 , -1.677495  , -1.8431272 , -2.028836  ,
        -2.0363647 , -1.9485295 , -1.5043341 ,      np.nan, -2.5527822 ,
        -2.5527822 , -2.4570104 , -2.4463632 , -2.5527822 ]])

bear_white_fur = np.array(
      [[ 2.229253 ,  2.4680387,  2.7017972,  2.8299874,  2.8676905,
         2.7746897,  2.4052003,  2.2795237,  2.1639012,  1.847196 ,
         2.0030351,  2.229253 ,     np.nan,  1.8044659,  1.8974666,
         2.0491517,  2.1326865,  2.3175294,  2.5112591,  2.9028799,
         2.7520679,  2.5962289,  2.2367936,  1.9577914,  1.8044659],
       [-1.0902537, -1.0601388, -1.1881273, -1.4641809, -1.677495 ,
        -1.8431272, -2.028836 , -2.0363647, -1.9485295, -1.5043341,
        -1.3186252, -1.0902537,     np.nan, -2.3902152, -2.5527822,
        -2.5527822, -2.4463632, -2.4570104, -2.5527822, -2.5527822,
        -2.2446597, -2.1467861, -2.3575907, -2.4378972, -2.3902152]])

bear_face = np.array(
      [[ 2.2419927,  2.2526567,  2.3015334,  2.3477442,  2.441943 ,
            np.nan,  2.5258499,  2.5113971,  2.5327621,  2.5632387,
         2.5780058,  2.5726645,  2.5475292,  2.5258499,     np.nan,
         2.2858075,  2.2704121,  2.2402497,  2.2283105,  2.2484187,
         2.273554 ,  2.2858075],
       [-1.7605035, -1.9432811, -1.9707865, -1.9654629, -1.781798 ,
            np.nan, -1.4688862, -1.4942957, -1.5099806, -1.5112354,
        -1.4877081, -1.466063 , -1.4588479, -1.4688862,     np.nan,
        -1.4346933, -1.4506918, -1.4463002, -1.418381 , -1.4055194,
        -1.4083427, -1.4346933]])import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la

bear_black = (0.141,0.11,0.11)
bear_white = (0.89,0.856,0.856)
magenta = (0xfc/255, 0x75/255, 0xdb/255) # Brighter magenta
orange = (218/255, 171/255, 115/255)
green = (175/255, 219/255, 133/255)
white = (240/255, 245/255, 250/255)
blue1 = (70/255, 101/255, 137/255)
blue2 = (122/255, 174/255, 215/255)

def gsBasis(A) :
    B = np.array(A, dtype=np.float_)
    B[:, 0] = B[:, 0] / la.norm(B[:, 0])
    B[:, 1] = B[:, 1] - B[:, 1] @ B[:, 0] * B[:, 0]
    if la.norm(B[:, 1]) > 1e-14 :
        B[:, 1] = B[:, 1] / la.norm(B[:, 1])
    else :
        B[:, 1] = np.zeros_like(B[:,1])
    return B

def draw_mirror(bearVectors) :
    fig,ax = plt.subplots(figsize=(12, 12), dpi= 80)
    ax.set_xlim([-3.50,3.50])
    ax.set_ylim([-3.50,3.50])
    ax.set_aspect(1)
    ax.set_axis_bgcolor(blue1)
    
    gs=gsBasis(bearVectors)
    ax.plot([gs[0,0]*-5,gs[0,0]*5],[gs[1,0]*-5,gs[1,0]*5], lw=2, color=green, zorder=4)
    ax.fill([
            -5*gs[0,0],-5*gs[0,0]-5*gs[0,1], 5*gs[0,0]-5*gs[0,1],5*gs[0,0]
        ],[
            -5*gs[1,0],-5*gs[1,0]-5*gs[1,1], 5*gs[1,0]-5*gs[1,1],5*gs[1,0]
        ], color=blue2, zorder=0)
    ax.arrow(0,0,bearVectors[0,0],bearVectors[1,0], lw=3, color=orange, zorder=5, head_width=0.1)
    ax.arrow(0,0,bearVectors[0,1],bearVectors[1,1], lw=3, color=orange, zorder=5, head_width=0.1)
    ax.arrow(0,0,gs[0,0],gs[1,0], lw=3, color=magenta, zorder=6, head_width=0.1)
    ax.arrow(0,0,gs[0,1],gs[1,1], lw=3, color=magenta, zorder=6, head_width=0.1)
    return ax

bear_black_fur = np.array(
      [[ 2.0030351 ,  2.229253  ,  2.1639012 ,  2.0809546 ,  1.9728726 ,
         1.8974666 ,  1.8924396 ,  2.0030351 ,      np.nan,  2.7017972 ,
         2.8500957 ,  2.9707453 ,  3.0159889 ,  2.94561   ,  2.8299874 ,
         2.7017972 ,      np.nan,  2.1639012 ,  2.2317666 ,  2.3147132 ,
         2.299632  ,  2.2493613 ,  2.1890365 ,  2.1211711 ,  2.1337387 ,
         2.1639012 ,      np.nan,  2.4982011 ,  2.5610936 ,  2.6213642 ,
         2.633986  ,  2.5536071 ,  2.5057417 ,  2.4982011 ,      np.nan,
         2.2468478 ,  2.3247673 ,  2.4429034 ,  2.4303357 ,  2.3448755 ,
         2.2820372 ,  2.2468478 ,      np.nan,  2.1966706 ,  2.2722074 ,
         2.4055076 ,  2.481933  ,  2.449941  ,  2.4001756 ,  2.3237501 ,
         2.222442  ,  2.1984479 ,  2.1966706 ,      np.nan,  1.847196  ,
         1.7818441 ,  1.7290599 ,  1.6310321 ,  1.4575984 ,  1.3369488 ,
         1.2791375 ,  1.3671112 ,  1.8044659 ,  1.9577914 ,  2.2367936 ,
         2.5962289 ,  2.7520679 ,  2.9028799 ,  3.4005595 ,  3.3150993 ,
         3.0511783 ,  2.9531506 ,  2.8676905 ,  2.7746897 ,  2.4052003 ,
         2.2795237 ,  2.1639012 ,  1.847196  ,      np.nan,  2.0491517 ,
         2.5112591 ,  2.3175294 ,  2.1326865 ,  2.0491517 ],
       [-1.3186252 , -1.0902537 , -0.99238015, -0.96477475, -0.99488975,
        -1.1153494 , -1.2408283 , -1.3186252 ,      np.nan, -1.1881273 ,
        -1.0852346 , -1.1454645 , -1.3286636 , -1.4666904 , -1.4641808 ,
        -1.1881273 ,      np.nan, -1.5545256 , -1.5219011 , -1.4014413 ,
        -1.3512497 , -1.3412115 , -1.3989317 , -1.4917862 , -1.5419777 ,
        -1.5545256 ,      np.nan, -1.4265371 , -1.3964222 , -1.4968054 ,
        -1.6097363 , -1.64738   , -1.5545256 , -1.4265371 ,      np.nan,
        -1.6423608 , -1.6699662 , -1.677495  , -1.7176483 , -1.7477632 ,
        -1.7176483 , -1.6423608 ,      np.nan, -1.7223509 , -1.7622781 ,
        -1.7764744 , -1.7613908 , -1.8767359 , -1.9805465 , -1.9991791 ,
        -1.9672374 , -1.913114  , -1.7223509 ,      np.nan, -1.5043341 ,
        -1.5444873 , -1.486767  , -1.1504836 , -1.0626484 , -1.11284   ,
        -1.2558858 , -1.7452537 , -2.3902152 , -2.4378972 , -2.3575907 ,
        -2.1467861 , -2.2446597 , -2.5527822 , -2.5527822 , -2.1919586 ,
        -1.7828973 , -1.6850238 , -1.677495  , -1.8431272 , -2.028836  ,
        -2.0363647 , -1.9485295 , -1.5043341 ,      np.nan, -2.5527822 ,
        -2.5527822 , -2.4570104 , -2.4463632 , -2.5527822 ]])

bear_white_fur = np.array(
      [[ 2.229253 ,  2.4680387,  2.7017972,  2.8299874,  2.8676905,
         2.7746897,  2.4052003,  2.2795237,  2.1639012,  1.847196 ,
         2.0030351,  2.229253 ,     np.nan,  1.8044659,  1.8974666,
         2.0491517,  2.1326865,  2.3175294,  2.5112591,  2.9028799,
         2.7520679,  2.5962289,  2.2367936,  1.9577914,  1.8044659],
       [-1.0902537, -1.0601388, -1.1881273, -1.4641809, -1.677495 ,
        -1.8431272, -2.028836 , -2.0363647, -1.9485295, -1.5043341,
        -1.3186252, -1.0902537,     np.nan, -2.3902152, -2.5527822,
        -2.5527822, -2.4463632, -2.4570104, -2.5527822, -2.5527822,
        -2.2446597, -2.1467861, -2.3575907, -2.4378972, -2.3902152]])

bear_face = np.array(
      [[ 2.2419927,  2.2526567,  2.3015334,  2.3477442,  2.441943 ,
            np.nan,  2.5258499,  2.5113971,  2.5327621,  2.5632387,
         2.5780058,  2.5726645,  2.5475292,  2.5258499,     np.nan,
         2.2858075,  2.2704121,  2.2402497,  2.2283105,  2.2484187,
         2.273554 ,  2.2858075],
       [-1.7605035, -1.9432811, -1.9707865, -1.9654629, -1.781798 ,
            np.nan, -1.4688862, -1.4942957, -1.5099806, -1.5112354,
        -1.4877081, -1.466063 , -1.4588479, -1.4688862,     np.nan,
        -1.4346933, -1.4506918, -1.4463002, -1.418381 , -1.4055194,
        -1.4083427, -1.4346933]])
