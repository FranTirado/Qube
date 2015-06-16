__author__ = 'alberto.sierra'

import qb

def main():
    # Introducimos los IDs de los JOBs.
    jobID = raw_input('Introduce el ID del Primer Job: ')
    jobID2 = raw_input('Introduce el ID del Segundo Job: ')



    # Gather all the information
    job = qb.jobinfo(fields=['agenda', 'subjobs', 'callbacks'], id=[jobID])
    job2 = qb.jobinfo(fields=['agenda', 'subjobs', 'callbacks'], id=[jobID2])

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

    # Asignamos las variables a la informacion del Qube del segundo Job
    jobName2 = job2[0]['name']
    assetVersion2 = job2[0]['package']['assetVersion']
    jobPreset2 = job2[0]['package']['render_preset']
    jobUser2 = job2[0]['user']
    mayaFile2 = job2[0]['package']['mayafile']
    joblayer2 = job2[0]['package']['render_layer']
    jobCamera2 = job2[0]['package']['selected_camera']
    jobRange2 = job2[0]['package']['range']
    jobResolution2 = job2[0]['package']['preset_resolution']

    # Compare all the gather information

    print ""
    print 'Name'
    print '1- ' + jobName + '\n2- ' + jobName2
    print ""
    print 'AssetVersion'
    print '1- ' + assetVersion + '\n2- ' + assetVersion2
    print ""
    print 'Preset'
    print '1- ' + jobPreset + '\n2- ' + jobPreset2
    print ""
    print 'User'
    print '1- ' + jobUser + '\n2- ' + jobUser2
    print ""
    print 'Layer'
    print '1- ' + joblayer + '\n2- ' + joblayer2
    print ""
    print 'MayaFile'
    print '1- ' + mayaFile + '\n2- ' + mayaFile2
    print ""
    print 'Camera'
    print '1- ' + jobCamera + '\n2- ' + jobCamera2
    print ''
    print 'Range'
    print '1- ' + jobRange + '\n2- ' + jobRange2
    print ''
    print 'Resolution'
    print '1- ' + jobResolution + '\n2- ' + jobResolution
    print ''

    # Comparing all. Falta por depurar esto, por que es una guarreria
    if jobName == jobName2:
       if assetVersion == assetVersion2:
           if jobPreset == jobPreset2:
               if jobUser == jobUser2:
                   if joblayer == joblayer2:
                       if mayaFile == mayaFile2:
                           if jobCamera == jobCamera2:
                               if jobRange == jobRange2:
                                   if jobResolution == jobResolution2:
                                        print 'It seems the same'
                                   else:
                                        print 'Algo es distinto'
                               else:
                                    print 'Algo es distinto'
                           else:
                               print 'Algo es distinto'
                       else:
                           print 'Algo es distinto'
                   else:
                       print 'Algo es distinto'
               else:
                   print 'Algo es distinto'
           else:
               print 'Algo es distinto'
       else:
           print 'Algo es distinto'
    else:
       print 'Algo es distinto'

    # if jobName == jobName2:
    #     print''
    #     print 'La camara es igual'
    # else:
    #     print''
    #     print 'La camara es distinta'
    #
    # if assetVersion == assetVersion2:
    #     print''
    #     print 'El asset es igual'
    # else:
    #     print''
    #     print 'El asset es distinto'
    #
    # if jobPreset == jobPreset2:
    #     print''
    #     print 'El preset es igual'
    # else:
    #     print''
    #     print 'El preset es distinto'
    #
    # if jobUser == jobUser2:
    #     print''
    #     print 'El User es igual'
    # else:
    #     print''
    #     print 'El User es distinto'
    #
    # if joblayer == joblayer2:
    #     print''
    #     print 'La Layer es igual'
    # else:
    #     print''
    #     print 'La Layer es distinta'
    #
    # if mayaFile == mayaFile2:
    #     print''
    #     print 'El archivo de Maya es igual'
    # else:
    #     print''
    #     print 'El archivo de Maya es distinto'
    #
    # if jobCamera == jobCamera2:
    #     print''
    #     print 'La Camara es igual'
    # else:
    #     print''
    #     print 'La Camara es distinta'

    print ''
