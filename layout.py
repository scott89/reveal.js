import os
import numpy as np
data_path = 'depth_res/'
img_names = os.listdir('../res/')
img_names = [i[:-4] for i in img_names if i.endswith('npy')]
for im_name in img_names:
    print('<section>')
    points = np.load('../res/'+im_name + '.npy')
    num = points.shape[0]
    # First slide
    print('<section>')
    print('<div>')

    print '<div style="float: left; width 50%">'
    print '<p>Input Image</p>'
    print('<img width="300" data-src="%s%s_img.png">'%(data_path, im_name))
    print('</div>')

    print '<div class="right" style="float: right; width 50%">'
    print '<div style="float: left">'
    print '<p>GT</p>'
    print('<img width="300" data-src="%s%s_gt.png">'%(data_path, im_name))
    print('</div>')

    print '<div style="float: right">'
    print '<p>Predict</p>'
    print('<img width="300" data-src="%s%s_GoogLeNet_v2.png">' % (data_path, im_name))
    print('</div>')
    print('</div>')
    print('</div>')
    print('</section>')
    for id in range(num):
        print('<section>')
        print('<div>')

        print '<div style="float: left; width 50%">'
        print '<p>Input Image</p>'
        print('<img width="300" data-src="%s%s_img_%d.png">' % ('focal_point/', im_name, id))
        print('</div>')

        print '<div class="right" style="float: right; width 50%">'
        print '<div style="float: left">'
        print '<p>GT</p>'
        print('<img width="300" data-src="res/%s_gt_%d.png">' % (im_name, id))
        print '<p>Aperture: 9pix</p>'
        print('</div>')

        print '<div style="float: right">'
        print '<p>Predict</p>'
        print('<img width="300" data-src="res/%s_GoogLeNet_%d.png">' % (im_name, id))
        print '<p>Aperture: 9pix</p>'
        print('</div>')
        print('</div>')
        print('</div>')
        print('</section>')

        ##
        print('<section>')
        print('<div>')

        print '<div style="float: left; width 50%">'
        print '<p>Input Image</p>'
        print('<img width="300" data-src="%s%s_img_%d.png">' % ('focal_point/', im_name, id))
        print('</div>')

        print '<div class="right" style="float: right; width 50%">'
        print '<div style="float: left">'
        print '<p>GT</p>'
        print('<img width="300" data-src="res/%s_gt_%d_2r.png">' % (im_name, id))
        print '<p>Aperture: 17pix</p>'
        print('</div>')

        print '<div style="float: right">'
        print '<p>Predict</p>'
        print('<img width="300" data-src="res/%s_GoogLeNet_%d_2r.png">' % (im_name, id))
        print '<p>Aperture: 17pix</p>'
        print('</div>')
        print('</div>')
        print('</div>')
        print('</section>')

    print('</section>')

'''
<section>
<div>
	<div style="float: left; width 50%">
		<p>Input Image</p>
		<img width="300" data-src="../res/ji_1148_GoogLeNet_0.png" alt="Down arrow" id='left_p'>
	</div>
	<div class="right" style="float: right; width 50%">
		<div style="float: left">
		<p>GT</p>
		<img width="300" data-src="../res/ji_1148_GoogLeNet_0.png" alt="Down arrow">
		</div>

		<div style="float: right">
		<p>Predicted</p>
		<img width="300" data-src="../res/ji_1148_GoogLeNet_0.png" alt="Down arrow">
		</div>
	</div>
</div>	
</section>
'''