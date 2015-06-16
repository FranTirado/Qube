__author__ = 'alberto.sierra'

import qb

def main():
    # Introducimos los IDs de los JOBs.
    jobID = raw_input('Introduce el ID Job: ')


    # Gather all the information
    job = qb.jobinfo(fields=['agenda', 'subjobs', 'callbacks'], id=[jobID])

    # Asignamos las variables a la informacion del Qube del primer Job
    jobName = job[0]['name']
    assetVersion = job[0]['package']['assetVersion']
    jobPreset = job[0]['package']['render_preset']
    jobUser = job[0]['user']
    mayaFile = job[0]['package']['mayafile']
    joblayer = job[0]['package']['render_layer']
    jobCamera = job[0]['package']['selected_camera']
    jobRange = job[0]['package']['range']
    jobResolution = job[0]['package']['preset_resolution']


    # Compare all the gather information

    print ""
    print 'Name'
    print jobName
    print ""
    print 'AssetVersion'
    print assetVersion
    print ""
    print 'Preset'
    print jobPreset
    print ""
    print 'User'
    print jobUser
    print ""
    print 'Layer'
    print joblayer
    print ""
    print 'MayaFile'
    print mayaFile
    print ""
    print 'Camera'
    print jobCamera
    print ''
    print 'Range'
    print jobRange
    print ''
    print 'Resolution'
    print jobResolution
    print ''
