import bpy

from .. utility import *

def init(self, prev_container):

    #TODO - JSON classes
    export.scene = """scene.camera.cliphither = 0.1
scene.camera.clipyon = 100
scene.camera.shutteropen = 0
scene.camera.shutterclose = 1
scene.camera.autovolume.enable = 1
scene.camera.lookat.orig = 7.358891 -6.925791 4.958309
scene.camera.lookat.target = 6.707333 -6.31162 4.513038
scene.camera.up = -0.3240135 0.3054208 0.8953956
scene.camera.screenwindow = -1 1 -0.5625 0.5625
scene.camera.lensradius = 0
scene.camera.focaldistance = 10
scene.camera.autofocus.enable = 0
scene.camera.type = "perspective"
scene.camera.oculusrift.barrelpostpro.enable = 0
scene.camera.fieldofview = 39.59776
scene.camera.bokeh.blades = 0
scene.camera.bokeh.power = 3
scene.camera.bokeh.distribution.type = "NONE"
scene.camera.bokeh.scale.x = 0.7071068
scene.camera.bokeh.scale.y = 0.7071068
scene.lights.__WORLD_BACKGROUND_LIGHT__.gain = 2e-05 2e-05 2e-05
scene.lights.__WORLD_BACKGROUND_LIGHT__.transformation = 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1
scene.lights.__WORLD_BACKGROUND_LIGHT__.id = 0
scene.lights.__WORLD_BACKGROUND_LIGHT__.temperature = -1
scene.lights.__WORLD_BACKGROUND_LIGHT__.temperature.normalize = 0
scene.lights.__WORLD_BACKGROUND_LIGHT__.visibility.indirect.diffuse.enable = 1
scene.lights.__WORLD_BACKGROUND_LIGHT__.visibility.indirect.glossy.enable = 1
scene.lights.__WORLD_BACKGROUND_LIGHT__.visibility.indirect.specular.enable = 1
scene.lights.__WORLD_BACKGROUND_LIGHT__.type = "sky2"
scene.lights.__WORLD_BACKGROUND_LIGHT__.dir = 0 0 1
scene.lights.__WORLD_BACKGROUND_LIGHT__.turbidity = 2.2
scene.lights.__WORLD_BACKGROUND_LIGHT__.groundalbedo = 0.5 0.5 0.5
scene.lights.__WORLD_BACKGROUND_LIGHT__.ground.enable = 0
scene.lights.__WORLD_BACKGROUND_LIGHT__.ground.color = 0.5 0.5 0.5
scene.lights.__WORLD_BACKGROUND_LIGHT__.ground.autoscale = 1
scene.lights.__WORLD_BACKGROUND_LIGHT__.distribution.width = 512
scene.lights.__WORLD_BACKGROUND_LIGHT__.distribution.height = 256
scene.lights.__WORLD_BACKGROUND_LIGHT__.visibilitymapcache.enable = 0
scene.lights.2382361116072.gain = 1 1 1
scene.lights.2382361116072.transformation = -0.2908646 0.9551712 -0.05518906 0 -0.7711008 -0.1998834 0.6045247 0 0.5663932 0.2183912 0.7946723 0 4.076245 1.005454 5.903862 1
scene.lights.2382361116072.id = 0
scene.lights.2382361116072.temperature = -1
scene.lights.2382361116072.temperature.normalize = 0
scene.lights.2382361116072.type = "sphere"
scene.lights.2382361116072.color = 1 1 1
scene.lights.2382361116072.power = 0
scene.lights.2382361116072.normalizebycolor = 0
scene.lights.2382361116072.efficency = 0
scene.lights.2382361116072.position = 0 0 0
scene.lights.2382361116072.radius = 0.1
scene.materials.Material2382357175256.type = "disney"
scene.materials.Material2382357175256.basecolor = "0.7 0.7 0.7"
scene.materials.Material2382357175256.subsurface = "0"
scene.materials.Material2382357175256.roughness = "0.2"
scene.materials.Material2382357175256.metallic = "0"
scene.materials.Material2382357175256.specular = "0.5"
scene.materials.Material2382357175256.speculartint = "0"
scene.materials.Material2382357175256.clearcoat = "0"
scene.materials.Material2382357175256.clearcoatgloss = "1"
scene.materials.Material2382357175256.anisotropic = "0"
scene.materials.Material2382357175256.sheen = "0"
scene.materials.Material2382357175256.sheentint = "0"
scene.materials.Material2382357175256.transparency.shadow = 0 0 0
scene.materials.Material2382357175256.id = 3364224
scene.materials.Material2382357175256.emission.gain = 1 1 1
scene.materials.Material2382357175256.emission.power = 0
scene.materials.Material2382357175256.emission.normalizebycolor = 1
scene.materials.Material2382357175256.emission.efficency = 0
scene.materials.Material2382357175256.emission.theta = 90
scene.materials.Material2382357175256.emission.id = 0
scene.materials.Material2382357175256.emission.importance = 1
scene.materials.Material2382357175256.emission.temperature = -1
scene.materials.Material2382357175256.emission.temperature.normalize = 0
scene.materials.Material2382357175256.emission.directlightsampling.type = "AUTO"
scene.materials.Material2382357175256.visibility.indirect.diffuse.enable = 1
scene.materials.Material2382357175256.visibility.indirect.glossy.enable = 1
scene.materials.Material2382357175256.visibility.indirect.specular.enable = 1
scene.materials.Material2382357175256.shadowcatcher.enable = 0
scene.materials.Material2382357175256.shadowcatcher.onlyinfinitelights = 0
scene.materials.Material2382357175256.photongi.enable = 1
scene.materials.Material2382357175256.holdout.enable = 0
scene.materials.Material__0012382357172440.type = "disney"
scene.materials.Material__0012382357172440.basecolor = "0.7 0.7 0.7"
scene.materials.Material__0012382357172440.subsurface = "0"
scene.materials.Material__0012382357172440.roughness = "0.2"
scene.materials.Material__0012382357172440.metallic = "0"
scene.materials.Material__0012382357172440.specular = "0.5"
scene.materials.Material__0012382357172440.speculartint = "0"
scene.materials.Material__0012382357172440.clearcoat = "0"
scene.materials.Material__0012382357172440.clearcoatgloss = "1"
scene.materials.Material__0012382357172440.anisotropic = "0"
scene.materials.Material__0012382357172440.sheen = "0"
scene.materials.Material__0012382357172440.sheentint = "0"
scene.materials.Material__0012382357172440.transparency.shadow = 0 0 0
scene.materials.Material__0012382357172440.id = 6728256
scene.materials.Material__0012382357172440.emission.gain = 1 1 1
scene.materials.Material__0012382357172440.emission.power = 0
scene.materials.Material__0012382357172440.emission.normalizebycolor = 1
scene.materials.Material__0012382357172440.emission.efficency = 0
scene.materials.Material__0012382357172440.emission.theta = 90
scene.materials.Material__0012382357172440.emission.id = 0
scene.materials.Material__0012382357172440.emission.importance = 1
scene.materials.Material__0012382357172440.emission.temperature = -1
scene.materials.Material__0012382357172440.emission.temperature.normalize = 0
scene.materials.Material__0012382357172440.emission.directlightsampling.type = "AUTO"
scene.materials.Material__0012382357172440.visibility.indirect.diffuse.enable = 1
scene.materials.Material__0012382357172440.visibility.indirect.glossy.enable = 1
scene.materials.Material__0012382357172440.visibility.indirect.specular.enable = 1
scene.materials.Material__0012382357172440.shadowcatcher.enable = 0
scene.materials.Material__0012382357172440.shadowcatcher.onlyinfinitelights = 0
scene.materials.Material__0012382357172440.photongi.enable = 1
scene.materials.Material__0012382357172440.holdout.enable = 0
scene.objects.23823611086320.material = "Material2382357175256"
scene.objects.23823611086320.ply = "mesh-00000.ply"
scene.objects.23823611086320.camerainvisible = 0
scene.objects.23823611086320.id = 1326487202
scene.objects.23823611086320.appliedtransformation = 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 1
scene.objects.23823611279760.material = "Material__0012382357172440"
scene.objects.23823611279760.ply = "mesh-00001.ply"
scene.objects.23823611279760.camerainvisible = 0
scene.objects.23823611279760.id = 3772660237
scene.objects.23823611279760.appliedtransformation = 5 0 0 0 0 5 0 0 0 0 5 0 0 0 0 1
"""

    export.config = """context.verbose = 1
accelerator.type = "AUTO"
accelerator.instances.enable = 1
accelerator.motionblur.enable = 1
accelerator.bvh.builder.type = "EMBREE_BINNED_SAH"
accelerator.bvh.treetype = 4
accelerator.bvh.costsamples = 0
accelerator.bvh.isectcost = 80
accelerator.bvh.travcost = 10
accelerator.bvh.emptybonus = 0.5
scene.epsilon.min = "1e-05"
scene.epsilon.max = "0.1"
scene.file = "scene.scn"
images.scale = 1
lightstrategy.type = "LOG_POWER"
native.threads.count = 8
renderengine.type = "BAKECPU"
path.pathdepth.total = "7"
path.pathdepth.diffuse = "5"
path.pathdepth.glossy = "5"
path.pathdepth.specular = "6"
path.hybridbackforward.enable = "0"
path.hybridbackforward.partition = "0.8"
path.hybridbackforward.glossinessthreshold = "0.049"
path.russianroulette.depth = 3
path.russianroulette.cap = 0.5
path.clamping.variance.maxvalue = 0
path.forceblackbackground.enable = "0"
sampler.type = "SOBOL"
sampler.imagesamples.enable = 1
sampler.sobol.adaptive.strength = "0.9"
sampler.sobol.adaptive.userimportanceweight = 0.75
sampler.sobol.bucketsize = "16"
sampler.sobol.tilesize = "16"
sampler.sobol.supersampling = "1"
sampler.sobol.overlapping = "1"
path.photongi.sampler.type = "METROPOLIS"
path.photongi.photon.maxcount = 100000000
path.photongi.photon.maxdepth = 4
path.photongi.photon.time.start = 0
path.photongi.photon.time.end = -1
path.photongi.visibility.lookup.radius = 0
path.photongi.visibility.lookup.normalangle = 10
path.photongi.visibility.targethitrate = 0.99
path.photongi.visibility.maxsamplecount = 1048576
path.photongi.glossinessusagethreshold = 0.05
path.photongi.indirect.enabled = 0
path.photongi.indirect.maxsize = 0
path.photongi.indirect.haltthreshold = 0.05
path.photongi.indirect.lookup.radius = 0
path.photongi.indirect.lookup.normalangle = 10
path.photongi.indirect.usagethresholdscale = 8
path.photongi.indirect.filter.radiusscale = 3
path.photongi.caustic.enabled = 0
path.photongi.caustic.maxsize = 100000
path.photongi.caustic.updatespp = 8
path.photongi.caustic.updatespp.radiusreduction = 0.96
path.photongi.caustic.updatespp.minradius = 0.003
path.photongi.caustic.lookup.radius = 0.15
path.photongi.caustic.lookup.normalangle = 10
path.photongi.debug.type = "none"
path.photongi.persistent.file = ""
path.photongi.persistent.safesave = 1
film.filter.type = "BLACKMANHARRIS"
film.filter.width = 2
opencl.platform.index = -1
film.width = 960
film.height = 600
film.safesave = 1
film.noiseestimation.step = "32"
film.noiseestimation.warmup = "8"
film.noiseestimation.filter.scale = 4
batch.haltnoisethreshold = 0.01
batch.haltnoisethreshold.step = 64
batch.haltnoisethreshold.warmup = 64
batch.haltnoisethreshold.filter.enable = 1
batch.haltnoisethreshold.stoprendering.enable = 1
batch.halttime = "0"
batch.haltspp = 32
film.outputs.safesave = 1
film.outputs.0.type = "RGB_IMAGEPIPELINE"
film.outputs.0.filename = "RGB_IMAGEPIPELINE_0.png"
film.outputs.0.index = "0"
film.imagepipelines.000.0.type = "NOP"
film.imagepipelines.000.1.type = "TONEMAP_LINEAR"
film.imagepipelines.000.1.scale = "1"
film.imagepipelines.000.2.type = "GAMMA_CORRECTION"
film.imagepipelines.000.2.value = "2.2"
film.imagepipelines.000.radiancescales.0.enabled = "1"
film.imagepipelines.000.radiancescales.0.globalscale = "1"
film.imagepipelines.000.radiancescales.0.rgbscale = "1" "1" "1"
periodicsave.film.outputs.period = 0
periodicsave.film.period = 0
periodicsave.film.filename = "film.flm"
periodicsave.resumerendering.period = 0
periodicsave.resumerendering.filename = "rendering.rsm"
resumerendering.filesafe = 1
debug.renderconfig.parse.print = 0
debug.scene.parse.print = 0
screen.refresh.interval = 100
screen.tool.type = "CAMERA_EDIT"
screen.tiles.pending.show = 1
screen.tiles.converged.show = 0
screen.tiles.notconverged.show = 0
screen.tiles.passcount.show = 0
screen.tiles.error.show = 0
bake.minmapautosize = 64
bake.maxmapautosize = 1024
bake.powerof2autosize.enable = 1
bake.skipexistingmapfiles = 1
film.imagepipelines.1.0.type = "NOP"
bake.maps.0.type = "COMBINED"
bake.maps.0.filename = "23823611086320.exr"
bake.maps.0.imagepipelineindex = 1
bake.maps.0.width = 512
bake.maps.0.height = 512
bake.maps.0.autosize.enabled = 1
bake.maps.0.uvindex = 0
bake.maps.0.objectnames = "23823611086320"
bake.maps.1.type = "COMBINED"
bake.maps.1.filename = "23823611279760.exr"
bake.maps.1.imagepipelineindex = 1
bake.maps.1.width = 512
bake.maps.1.height = 512
bake.maps.1.autosize.enabled = 1
bake.maps.1.uvindex = 0
bake.maps.1.objectnames = "23823611279760"
"""