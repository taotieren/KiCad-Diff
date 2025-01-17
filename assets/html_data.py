
# HTML Data
# Intermediate approach before something better

tail = '''
<div class="clearfix"></div>
<div style="padding:6px;"></div>
'''

indexHead = '''
<!DOCTYPE HTML>
<html lang="en">
<meta charset="utf-8" />
<head>
    <title>{TITLE}</title>
    <link rel="icon" href="http://127.0.0.1:9092/favicon.ico" type="image/x-icon" />
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
    <link rel="stylesheet" type="text/css" href="style.css" media="screen" />
</head>
<div class="responsivefull">
    <table style="border-color: #aaaaaa; width: 100%; height: 2px;" border="2px" cellspacing="2px" cellpadding="3px">
        <tbody>
            <tr>
                <td colspan="3" rowspan="3" width="45%">
                    <div class="title"> Title: {TITLE} </div>
                    <div class="details"> Company: {COMPANY} </div>
                </td>
                <td width="25%">
                    <div class="versions">Thickness (mm)</div>
                </td>
                <td width="15%">
                    <div class="versions green">{THICK1}</div>
                </td>
                <td width="15%">
                    <div class="versions red">{THICK2}</div>
                </td>
            </tr>
            <td width="25%">
                <div class="versions">Modules</div>
            </td>
            <td width="15%">
                <div class="versions green">{MODULES1}</div>
            </td>
            <td width="15%">
                <div class="versions red">{MODULES2}</div>
            </td>
            <tr>
                <td width="25%">
                    <div class="versions">Drawings</div>
                </td>
                <td width="15%">
                    <div class="versions green">{DRAWINGS1}</div>
                </td>
                <td width="15%">
                    <div class="versions red">{DRAWINGS2}</div>
                </td>
            </tr>
            <tr>
                <td width="15%">
                    <div class="versions">Version</div>
                </td>
                <td width="15%">
                    <div class="versions green">{diffDir1}</div>
                </td>
                <td width="15%">
                    <div class="versions red">{diffDir2}</div>
                </td>
                <td width="25%">
                    <div class="versions">Nets</div>
                </td>
                <td width="15%">
                    <div class="versions green">{NETS1}</div>
                </td>
                <td width="15%">
                    <div class="versions red">{NETS2}</div>
                </td>
            </tr>
            <tr>
                <td width="15%">
                    <div class="versions">Date</div>
                </td>
                <td width="15%">
                    <div class="versions">{D1DATE}</div>
                </td>
                <td width="15%">
                    <div class="versions">{D2DATE}</div>
                </td>
                <td width="25%">
                    <div class="versions">Tracks</div>
                </td>
                <td width="15%">
                    <div class="versions green">{TRACKS1}</div>
                </td>
                <td width="15%">
                    <div class="versions red">{TRACKS2}</div>
                </td>
            </tr>
            <tr>
                <td width="15%">
                    <div class="versions">Time</div>
                </td>
                <td width="15%">
                    <div class="versions">{D1TIME}</div>
                </td>
                <td width="15%">
                    <div class="versions">{D2TIME}</div>
                </td>
                <td width="25%">
                    <div class="versions">Zones</div>
                </td>
                <td width="15%">
                    <div class="versions green">{ZONES1}</div>
                </td>
                <td width="15%">
                    <div class="versions red">{ZONES2}</div>
                </td>
            </tr>
        </tbody>
    </table>
</div>
'''

outfile = '''
<div class="responsive">
  <div class="gallery">
    <a target="_blank" href=../{diff1}/{layername}>
    <a href=./triptych/{prj}-{layer}.html> <img class="{layer}" src=../{diff1}/{layername} height="200"> </a>
    </a>
    <div class="desc">{layer}</div>
  </div>
</div>
'''

triptychHTML = '''
<!DOCTYPE HTML>
<html lang="en">
<meta charset="utf-8" />
<head>
<link rel="stylesheet" type="text/css" href="../style.css" media="screen" />
<style>
div.responsive {{
   padding: 0 6px;
   float: left;
   width: 49.99%;
   }}
</style>
    <script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.0/dist/svg-pan-zoom.min.js"></script>
</head>
<body>
<div class="title">{prj}</div>
<div class="subtitle">{layer}</div>


     <div id="compo-container" style="width: 100%; height: 800px;">
        <svg id="svg-id" xmlns="http://www.w3.org/2000/svg" style="display: inline; width: inherit; min-width: inherit; max-width: inherit; height: inherit; min-height: inherit; max-height: inherit;" version="1.1">
            <g>
                <svg id="compo">
                    <defs>
                        <filter id="f1">
                            <feColorMatrix id="c1" type="matrix" values="1   0   0   0   0
                  0   1   0   1   0
                  0   0   1   1   0
                  0   0   0   1   0 " />
                        </filter>
                    </defs>
                    <image x="0" y="0" height="100%" width="100%" filter="url(#f1)" xlink:href="../../{diff1}/{layername}" />
                </svg>

                <svg id="compo2">
                    <defs>
                        <filter id="f2">
                            <feColorMatrix id="c2" type="matrix" values="1   0   0   1   0
                  0   1   0   0   0
                  0   0   1   0   0
                  0   0   0   .5   0" />
                        </filter>
                    </defs>
                    <image x="0" y="0" height="100%" width="100%" filter="url(#f2)" xlink:href="../../{diff2}/{layername}" />
                </svg>
            </g>
        </svg>
    </div>

<div id="sbs-container"  width=100%; height=100% >
<embed id="diff1" class="{layer}" type="image/svg+xml" style="width: 50%; float: left; border:1px solid black;" src="../../{diff1}/{layername}" />
<embed id="diff2" class="{layer}" type="image/svg+xml" style="width: 50%; border:1px solid black;" src="../../{diff2}/{layername}" />
</div>

'''

twopane='''
<script>
        // Don't use window.onLoad like this in production, because it can only listen to one function.
        window.onload = function() {
            // Expose variable for testing purposes
            window.panZoomDiff = svgPanZoom('#svg-id', {
                zoomEnabled: true,
                controlIconsEnabled: true,
                center: true,
                minZoom: 1.5,
                maxZoom: 20,
            });
            // Expose variable to use for testing
            window.zoomDiff = svgPanZoom('#diff1', {
                zoomEnabled: true,
                controlIconsEnabled: true,
                minZoom: 1.5,
                maxZoom: 20,
                // Uncomment this in order to get Y asis synchronized pan
                // beforePan: function(oldP, newP) {return {y:false}},
            });

            // Expose variable to use for testing
            window.zoomDiff2 = svgPanZoom('#diff2', {
                zoomEnabled: true,
                controlIconsEnabled: true,
                minZoom: 1.5,
                maxZoom: 20,
            });

            zoomDiff.setOnZoom(function(level) {
                zoomDiff2.zoom(level)
                zoomDiff2.pan(zoomDiff.getPan())
            })

            zoomDiff.setOnPan(function(point) {
                zoomDiff2.pan(point)
            })

            zoomDiff2.setOnZoom(function(level) {
                zoomDiff.zoom(level)
                zoomDiff.pan(zoomDiff2.getPan())
            })

            zoomDiff2.setOnPan(function(point) {
                zoomDiff.pan(point)
            })

        };
</script>

</body>

</html>
''' 