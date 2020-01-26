<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-warn"></i> 权限测试</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <h1>管理员权限页面</h1>
            <p>只有用 admin 账号登录的才拥有管理员权限，才能进到看到该页面</p>
        </div>

    </div>
</template>

<script>
    export default {
        data: function(){
            return {}
        }
    }
</script>

<style scoped>
h1{
    text-align: center;
    margin: 30px 0;
}
p{
    line-height: 30px;
    margin-bottom: 10px;
    text-indent: 2em;
}
.logout{
    color: #409EFF;
}
</style>