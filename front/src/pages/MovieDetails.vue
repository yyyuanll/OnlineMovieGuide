<template>
    <div class="Stage">
        <div class="Details">
            <div class="left">
                <div class="title">
                电影名
                </div>
                <div class="poster">
                    <img src="../images/poster_example.jpg" alt="">
                </div>
                <div class="yearAndElse">
                    年份-评级-时长
                </div>
                <div class="IMDbRating">
                    IMDb评分
                </div>
                <div class="metascore">
                    Metascore
                </div>
                <div class="userRating">
                    用户评分
                </div>
                <div class="genre">
                    类型
                </div>
                <div class="director">
                    导演
                </div>
                <div class="writer">
                    编剧
                </div>
                <div class="actor">
                    演员
                </div>
            </div>
            <div class="right">
                <div class="comment">
                    <li><p>这电影真棒</p></li>
                    <li><p>垃圾电影</p></li>
                    <li><p>看的我睡着了</p></li>
                    <li><p>你们都没有童年吗</p></li>
                </div>
            </div>
        </div>
        <div class="recommend">
            推荐电影
        </div>
    </div>
</template>

<style>
    .left{
        float: left;
    }
    .right{
        float: right;
    }
    .Details{
        width: 90%;
        height: 440px;
        margin: 0 auto;
        background-color: #fff;
    }
    .Details .left{
        width: 50%;
    }
    .Details .right{
        width: 50%;
    }
    .Details .title{
        background-color: #fff;
        width: 80%;
        height: 100px;
        text-align: center;
        line-height: 100px;
        float: left;
        margin: 0;
    }
    .Details .poster{
        background-color: #fff;
        width: 20%;
        height: auto;
        float: right;
    }
    .Details .poster img{
        width: 100%;
        max-height: 240px;
    }
    .Details .yearAndElse{
        background-color: #fff;
        width: 80%;
        height: 20px;
        float: left;
        text-align: center;
        line-height: 20px;
    }
    .Details .IMDbRating, .metascore, .userRating{
        width: 26.66%;
        height: 100px;
        float: left;
        text-align: center;
        line-height: 100px;
        background-color: #fff;
    }
    .Details .genre{
        background-color: #fff;
        width: 80%;
        height: 20px;
        line-height: 20px;
        float: left;
    }
    .Details .director, .writer{
        background-color: #fff;
        width: 100%;
        height: 50px;
        line-height: 50px;
        float: left;
    }
    .Details .actor{
        background-color: #fff;
        width: 100%;
        height: 100px;
        line-height: 100px;
        float: left;
    }
    .Details .comment{
        width: 100%;
        background-color: #fff;
        height: 440px;
    }
    .comment li{
        height: 110px;
    }
    .recommend{
        width: 90%;
        margin: 0 auto;
        background-color: #f2f2f2;
        height: 100px;
    }
</style>