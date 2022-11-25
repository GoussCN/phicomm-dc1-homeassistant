switch:
  - platform: phicomm_dc1
    name: dc1_shufang
    ip: 192.168.9.44
    ports: {'1':'dc1_shufang_s1','2':'dc1_shufang_s2','3':'dc1_shufang_s3'}
  - platform: phicomm_dc1
    name: dc1_huayuan
    ip: 192.168.1.112
    ports: {'1':'dc1_huayuan_s1','2':'dc1_huayuan_s2','3':'dc1_huayuan_s3'}
  - platform: phicomm_dc1
    name: dc1_chufang
    ip: 192.168.0.113
    ports: {'1':'dc1_chufang_s1','2':'dc1_chufang_s2','3':'dc1_chufang_s3'}

sensor:
  - platform: template
    sensors:
      dc1_shufang_v:
        friendly_name: 当前电压
        value_template: "{{ states.switch.dc1_shufang.attributes.v }}"
        unit_of_measurement: V
      dc1_shufang_p:
        friendly_name: 当前功率
        value_template: "{{ states.switch.dc1_shufang.attributes.p }}"
        unit_of_measurement: W

  - platform: template
    sensors:
      dc1_huayuan_v:
        friendly_name: 当前电压
        value_template: "{{ states.switch.dc1_huayuan.attributes.v }}"
        unit_of_measurement: V
      dc1_huayuan_p:
        friendly_name: 当前功率
        value_template: "{{ states.switch.dc1_huayuan.attributes.p }}"
        unit_of_measurement: W

  - platform: template
    sensors:
      dc1_chufang_v:
        friendly_name: 当前电压
        value_template: "{{ states.switch.dc1_chufang.attributes.v }}"
        unit_of_measurement: V
      dc1_chufang_p:
        friendly_name: 当前功率
        value_template: "{{ states.switch.dc1_chufang.attributes.p }}"
        unit_of_measurement: W
