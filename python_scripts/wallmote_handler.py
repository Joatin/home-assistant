event = data.get('event')
label = data.get('label')
index = data.get('index')
node_id = int(data.get('node_id'))

# we only care about index == 10, the end of the swipe 'parameter'
# and for safety we also only look at valueChanged
if (index == '10') and event == 'valueChanged':
    value = int(data.get('value', '0'))
    # unpack byte 2 (button id)
    scene_id = value >> 24 & 0xff

    # unpack byte 3 (direction)
    scene_value_id = value >> 16 & 0xff
    # offset by 10 to avoid colissions
    scene_value_id = scene_value_id + 10

    scene_value_label = 'Swipe Down'
    if scene_value_id == 11:
        scene_value_label = 'Swipe Up'

    hass.bus.fire('ozw.scene_activated', {
        'node_id': node_id,
        'scene_id': scene_id,
        'scene_value_id': scene_value_id,
        'scene_value_label': scene_value_label,
    })
