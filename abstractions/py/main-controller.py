

# luis arandas 24-07-2022
# class for attributes extension

class MainController:

    def __init__(self):
        print("Controller initialisation")
        
        attr = op('attrAssign')

        attr.par.value0 = 0
        attr.par.value1 = 0
        attr.par.value2 = 0
        attr.par.value3 = 0
        attr.par.value4 = 0
        attr.par.value5 = 0

    def SimplePrint( self ):
        print( 'Hello World' )
        return





"""
class GenGeo:

    def __init__( self ):
        print( 'Gen Init' )
        attr = op('attrAssign')

        op('moviefilein1').par.file = app.samplesFolder + '/Map/TestPattern.jpg'

        attr.par.value4 = 0
        attr.par.value5 = 0
        attr.par.value6 = 1
        attr.par.value7 = 1
        return

    def SimplePrint( self ):
        print( 'Hello World' )
        return

    def TorusPar( self , rows , columns ):
        op('geo1/torus1').par.rows = rows
        op('geo1/torus1').par.cols = columns
        return

    def TorusParReset( self ):
        op('geo1/torus1').par.rows = 10
        op('geo1/torus1').par.cols = 20 
        return

    def Texture( self , file ): 
        op('moviefilein1').par.file = file
        return

    def TextureReset( self ):
        op('moviefilein1').par.file = app.samplesFolder + '/Map/TestPattern.jpg'
        return

    def Rot( self , rx , ry , rz ):
        attr = op('attrAssign')
 
        attr.par.value0 = rx
        attr.par.value1 = ry
        attr.par.value2 = rz
        return

    def RotReset( self ):
        attr = op('attrAssign')
        speed = op('speed1')
        filterCHOP = op('filter1')
        attr.par.value0 = 0
        attr.par.value1 = 0
        attr.par.value2 = 0
        speed.par.resetpulse.pulse()
        filterCHOP.par.resetpulse.pulse()
        return

    def TorusNoise( self , noiseAmp ):
        op( 'attrAssign' ).par.value3 = noiseAmp
        return

    def Mono( self , monoVal ):
        op( 'attrAssign' ).par.value4 = monoVal
        return

    def Levels( self , blkLvl , bright , opacity ):
        attr = op('attrAssign')
        attr.par.value5 = blkLvl
        attr.par.value6 = bright
        attr.par.value7 = opacity
        return

    def PostProcessReset( self ):
        attr = op('attrAssign')
        attr.par.value4 = 0
        attr.par.value5 = 0
        attr.par.value6 = 1
        attr.par.value7 = 1
        return

    def Background( self , onOff ):
        op('comp1').bypass = onOff
        return

"""