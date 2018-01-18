from lsst.obs.auxTel.ingest import AuxTelParseTask

config.parse.retarget(AuxTelParseTask)

config.parse.translation = {
    'expTime': 'EXPTIME',
    'object': 'OBJECT',
    'imageType': 'IMGTYPE',
    'testType': 'TESTTYPE',
    'filter': 'FILTER',
    'lsstSerial': 'LSST_NUM',
    'date': 'DATE-OBS',
    'dateObs': 'DATE-OBS',
}
config.parse.translators = {
    'visit': 'translate_visit',
    'wavelength': 'translate_wavelength',
}
config.parse.defaults = {
    'object': "UNKNOWN",
}
config.parse.hdu = 0

config.register.columns = {
    'run': 'text',
    'visit': 'int',
    'basename': 'text',
    'filter': 'text',
    'date': 'text',
    'dateObs': 'text',
    'expTime': 'double',
    'ccd': 'int',
    'object': 'text',
    'imageType': 'text',
    'testType': 'text',
    'lsstSerial': 'text',
    'field': 'text',
    'wavelength': 'int',
}
config.register.visit = list(config.register.columns.keys())
