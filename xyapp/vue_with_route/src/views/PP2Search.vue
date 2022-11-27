<!-- 说明：科研板块的搜索界面
内容：
因为是精细搜索，可以不显示从后端返回的其他内容，搜索条件出来了再在PP2Result页显示 -->

<template>
  <div class="home">
    <h1>
      <img src="@/assets/logo.svg">
    </h1>
    <h1>Tutor</h1>

    <h2>
      <p>
        <t style="margin-right: 95px">Academy & Institution</t><br>
        <el-cascader :options="options" :props="{ checkStrictly: true }" style="width: 260px; top: 5px" clearable>
        </el-cascader>
      </p>
      <p>
        <t style="margin-right: 180px">Academy</t><br>
        <el-select v-model="input1" filterable placeholder="" clearable>
          <el-option v-for="item in option1" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
      </p>
      <p>
        <t style="margin-right: 180px">Institution</t><br>
        <el-select v-model="input2" filterable placeholder="" clearable>
          <el-option v-for="item in option2" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
      </p>
      <p>
        <t style="margin-right: 180px">Professor</t><br>
        <el-input v-model="input3" placeholder="less than 25 characters" clearable>
        </el-input>
      </p>
      <p>
        <t style="margin-right: 195px">Starting</t><br>
        <el-date-picker v-model="input4" type="date" placeholder="请选择开始日期" style="width: 260px; top: 5px">
        </el-date-picker>

      </p>
    </h2>

    <el-button style="margin-left: 14%; " @click="Post()" type="text">
      <img src="@/assets/箭头一.svg">
    </el-button>

    <router-view></router-view>

    <navi-box></navi-box>

  </div>
</template>

<script>
import axios from "axios"
import NaviBox from '@/components/NaviBox.vue'
export default {
  components: { NaviBox },
  name: 'PP1Search',
  data() {
    return {
      input1: '',
      input2: '',
      input3: '',
      input4: '',
      options: [{
        value: 'zhinan',
        label: '指南',
        children: [{
          value: 'shejiyuanze',
          label: '设计原则',
          children: [{
            value: 'yizhi',
            label: '一致'
          }, {
            value: 'fankui',
            label: '反馈'
          }, {
            value: 'xiaolv',
            label: '效率'
          }, {
            value: 'kekong',
            label: '可控'
          }]
        }, {
          value: 'daohang',
          label: '导航',
          children: [{
            value: 'cexiangdaohang',
            label: '侧向导航'
          }, {
            value: 'dingbudaohang',
            label: '顶部导航'
          }]
        }]
      }, {
        value: 'zujian',
        label: '组件',
        children: [{
          value: 'basic',
          label: 'Basic',
          children: [{
            value: 'layout',
            label: 'Layout 布局'
          }, {
            value: 'color',
            label: 'Color 色彩'
          }, {
            value: 'typography',
            label: 'Typography 字体'
          }, {
            value: 'icon',
            label: 'Icon 图标'
          }, {
            value: 'button',
            label: 'Button 按钮'
          }]
        }, {
          value: 'form',
          label: 'Form',
          children: [{
            value: 'radio',
            label: 'Radio 单选框'
          }, {
            value: 'checkbox',
            label: 'Checkbox 多选框'
          }, {
            value: 'input',
            label: 'Input 输入框'
          }, {
            value: 'input-number',
            label: 'InputNumber 计数器'
          }, {
            value: 'select',
            label: 'Select 选择器'
          }, {
            value: 'cascader',
            label: 'Cascader 级联选择器'
          }, {
            value: 'switch',
            label: 'Switch 开关'
          }, {
            value: 'slider',
            label: 'Slider 滑块'
          }, {
            value: 'time-picker',
            label: 'TimePicker 时间选择器'
          }, {
            value: 'date-picker',
            label: 'DatePicker 日期选择器'
          }, {
            value: 'datetime-picker',
            label: 'DateTimePicker 日期时间选择器'
          }, {
            value: 'upload',
            label: 'Upload 上传'
          }, {
            value: 'rate',
            label: 'Rate 评分'
          }, {
            value: 'form',
            label: 'Form 表单'
          }]
        }, {
          value: 'data',
          label: 'Data',
          children: [{
            value: 'table',
            label: 'Table 表格'
          }, {
            value: 'tag',
            label: 'Tag 标签'
          }, {
            value: 'progress',
            label: 'Progress 进度条'
          }, {
            value: 'tree',
            label: 'Tree 树形控件'
          }, {
            value: 'pagination',
            label: 'Pagination 分页'
          }, {
            value: 'badge',
            label: 'Badge 标记'
          }]
        }, {
          value: 'notice',
          label: 'Notice',
          children: [{
            value: 'alert',
            label: 'Alert 警告'
          }, {
            value: 'loading',
            label: 'Loading 加载'
          }, {
            value: 'message',
            label: 'Message 消息提示'
          }, {
            value: 'message-box',
            label: 'MessageBox 弹框'
          }, {
            value: 'notification',
            label: 'Notification 通知'
          }]
        }, {
          value: 'navigation',
          label: 'Navigation',
          children: [{
            value: 'menu',
            label: 'NavMenu 导航菜单'
          }, {
            value: 'tabs',
            label: 'Tabs 标签页'
          }, {
            value: 'breadcrumb',
            label: 'Breadcrumb 面包屑'
          }, {
            value: 'dropdown',
            label: 'Dropdown 下拉菜单'
          }, {
            value: 'steps',
            label: 'Steps 步骤条'
          }]
        }, {
          value: 'others',
          label: 'Others',
          children: [{
            value: 'dialog',
            label: 'Dialog 对话框'
          }, {
            value: 'tooltip',
            label: 'Tooltip 文字提示'
          }, {
            value: 'popover',
            label: 'Popover 弹出框'
          }, {
            value: 'card',
            label: 'Card 卡片'
          }, {
            value: 'carousel',
            label: 'Carousel 走马灯'
          }, {
            value: 'collapse',
            label: 'Collapse 折叠面板'
          }]
        }]
      }, {
        value: 'ziyuan',
        label: '资源',
        children: [{
          value: 'axure',
          label: 'Axure Components'
        }, {
          value: 'sketch',
          label: 'Sketch Templates'
        }, {
          value: 'jiaohu',
          label: '组件交互文档'
        }]
      }],
      option1: [{
        value: '选项1',
        label: '数学科学学院'
      }, {
        value: '选项2',
        label: '物理学院'
      }, {
        value: '选项3',
        label: '化学与分子工程学院'
      }, {
        value: '选项4',
        label: '生命科学学院'
      }, {
        value: '选项5',
        label: '地球空间科学学院'
      }, {
        value: '选项6',
        label: '工学院',
        children: [{
          value: '子选项1',
          label: '理论与应用力学'
        }, {
          value: '子选项2',
          label: '工程与科学计算'
        }, {
          value: '子选项3',
          label: '能源工程科学'
        }, {
          value: '子选项4',
          label: '材料科学'
        }, {
          value: '子选项5',
          label: '生物医学工程'
        }]
      }, {
        value: '选项7',
        label: '信息科学技术学院'
      }],
      option2: [{
        value: '选项1',
        label: '黄金糕'
      }, {
        value: '选项2',
        label: '双皮奶'
      }, {
        value: '选项3',
        label: '蚵仔煎'
      }, {
        value: '选项4',
        label: '龙须面'
      }, {
        value: '选项5',
        label: '北京烤鸭'
      }],
    }
  },    
  methods: {
      Search() {
        if (this.input1 == "" || this.input2 == "" || this.input3 == "" || this.input4 == "") {
          alert("Please check your input")
        } else {
          axios.post('http://127.0.0.1:8000/json/markpost/', { academy: this.input1, institution: this.input2, professor: this.input3, starting_date: this.input4 })
            .then((response) => {
              console.log(response.data)
              if (response.data['status'] != 1) {
                alert(response.data['message'])
                this.$router.push('/');
              } else {
                alert(response.data['message'])
                this.$router.push('/PP2Search/PP2Result');
              }
           })
        }
      },
  },
}
</script>





<style scoped>
h2 {
  font: 1em sans-serif;
  margin: 80px 0px 60px;
}

a {
  color: #000000;
  margin: 32px;
}

h3 {
  margin: 0px 0px 60px;
}

.el-input {
  width: 260px;
  height: 32px;
  top: 5px;
  left: 0px;
}

.el-select {
  width: 260px;
  height: auto;
  top: 5px;
  left: 0px;
}
</style>