<template>
    <div class="Stage">
        <div class="Details">
            <div class="left">
                <div class="title">
                {{movieDetailes[0].title}}
                </div>
                <div class="poster">
                    <img v-bind:src="movieDetailes[0].image" alt="">
                </div>
                <div class="yearAndElse">
                    {{movieDetailes[0].year}}-{{movieDetailes[0].month}}-{{movieDetailes[0].day}}&nbsp;&nbsp;&nbsp;&nbsp;{{movieDetailes[0].rated}}&nbsp;&nbsp;&nbsp;&nbsp;{{movieDetailes[0].runtime}}
                </div>
                <div class="IMDbRating">
                    IMDb Score : {{movieDetailes[0].imdbrating}}
                </div>
                <div class="metascore">
                    Metascore : {{movieDetailes[0].metascore}}
                </div>
                <div class="userRating">
                    <span class="demonstration">User Score</span>
                    <el-rate
                        v-model="value2"
                        :colors="colors">
                    </el-rate>
                </div>
                <div class="genre">
                    Genre : {{movieDetailes[1].genre1}} {{movieDetailes[1].genre2}} {{movieDetailes[1].genre3}}
                </div>
                <div class="director">
                    Director : {{movieDetailes[0].director}}
                </div>
                <div class="writer">
                    Writer : {{movieDetailes[0].writer}}
                </div>
                <div class="actor">
                    Actor : 
                    <a v-bind:href="movieDetailes[4].actor_link1">{{movieDetailes[4].actor1}}</a> 、
                    <a v-bind:href="movieDetailes[4].actor_link2">{{movieDetailes[4].actor2}}</a> 、
                    <a v-bind:href="movieDetailes[4].actor_link3">{{movieDetailes[4].actor3}}</a> 、
                    <a v-bind:href="movieDetailes[4].actor_link4">{{movieDetailes[4].actor4}}</a>
                </div>
                <div class="recommend">
                    recommend
                </div>
            </div>
            <div class="right">
                <div class="comment">
                    <el-card><p>MasterPiece</p></el-card>
                    <el-card><p>Noob</p></el-card>
                    <el-card><p>Tiring</p></el-card>
                    <el-card class="commentForm">
                        <el-form ref="form" :model="form">
                            <el-form-item>
                                <el-input type="textarea" v-model="form.comment" placeholder="Enter your comment here!"></el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-button type="primary" @click="onSubmitComment" size="small">Upload Comment</el-button>
                            </el-form-item>
                        </el-form>
                    </el-card>
                </div>
            </div>
        </div>
        <!-- <div class="recommend">
            Recommand
        </div> -->
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
        width: 75%;
        height: 440px;
        margin: 0 auto;
        background-color: #fff;
    }
    .Details .left{
        width: 75%;
    }
    .Details .right{
        width: 25%;
    }
    .Details .title{
        background-color: #fff;
        width: 80%;
        height: 100px;
        text-align: center;
        line-height: 100px;
        float: left;
        margin: 0;
        font-size: 30px;
        font-weight: bold;
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
        height: 10px;
        float: left;
        text-align: center;
        line-height: 10px;
        font-size: 10px;
        font-style: italic;
    }
    .Details .IMDbRating, .metascore, .userRating{
        width: 26.66%;
        height: 110px;
        float: left;
        text-align: center;
        line-height: 110px;
        background-color: #fff;
    }
    .Details .userRating{
        line-height: 60px;
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
    .comment div{
        border: 0;
        margin: 10px 0;
    }
    .comment p{
        height: 24.5px;
    }
    .recommend{
        width: 100%;
        background-color: #f2f2f2;
        height: 100px;
        float: left;
    }
    .commentForm .el-card__body{
        height: 180px;
    }
</style>

<script>
import Axios from 'axios';
import { axiosInstance } from 'src/boot/axios';
import { dom } from 'quasar';
// import func from 'vue-editor-bridge';
    export default {
        data() {
            return {
                imdbid: 'tt0080684',
                username: 'Lucas Kim',
                value1: null,
                value2: null,
                colors: ['#99A9BF', '#F7BA2A', '#FF9900'],  // 等同于 { 2: '#99A9BF', 4: { value: '#F7BA2A', excluded: true }, 5: '#FF9900' }
                form: {
                        comment: '',
                    },
                movieDetailes:[
                    {
                        "title": "Star Wars: Episode V - The Empire Strikes Back",
                        "image": "http://127.0.0.1:8000/images/tt0080684.jpg",
                        "imdbrating": 8.8,
                        "imdbid": "tt0080684",
                        "metascore": 79,
                        "day": 20,
                        "month": 6,
                        "year": 1980,
                        "runtime": "124 min",
                        "rated": "PG",
                        "award": "Won 1 Oscar. Another 15 wins & 18 nominations.",
                        "director": "Irvin Kershner",
                        "writer": "Leigh Brackett (screenplay), Lawrence Kasdan (screenplay), George Lucas (story)"
                    },
                    {
                        "genre1": "Action",
                        "genre2": "Adventure",
                        "genre3": "Fantasy"
                    },
                    {
                        "language1": "English"
                    },
                    {
                        "country1": "USA"
                    },
                    {
                        "actor1": "Mark Hamill",
                        "actor_link1": "https://en.wikipedia.org/wiki/Mark_Hamill",
                        "actor2": "Harrison Ford",
                        "actor_link2": "https://en.wikipedia.org/wiki/Harrison_Ford",
                        "actor3": "Carrie Fisher",
                        "actor_link3": "https://en.wikipedia.org/wiki/Carrie_Fisher",
                        "actor4": "Billy Dee Williams",
                        "actor_link4": "https://en.wikipedia.org/wiki/Billy_Dee_Williams"
                    },
                    {},
                    {
                        "imdbid": "tt0082288",
                        "title": "Dragonslayer",
                        "img": "http://127.0.0.1:8000/images/tt0082288.jpg"
                    },
                    {
                        "imdbid": "tt0084749",
                        "title": "The Sword and the Sorcerer",
                        "img": "http://127.0.0.1:8000/images/tt0084749.jpg"
                    },
                    {
                        "imdbid": "tt0083630",
                        "title": "The Beastmaster",
                        "img": "http://127.0.0.1:8000/images/tt0083630.jpg"
                    },
                    {
                        "imdbid": "tt0085811",
                        "title": "Krull",
                        "img": "http://127.0.0.1:8000/images/tt0085811.jpg"
                    },
                    {
                        "imdbid": "tt0087078",
                        "title": "Conan the Destroyer",
                        "img": "http://127.0.0.1:8000/images/tt0087078.jpg"
                    }
                ]
                
            }
        },
        created(){
            // this.getImdbID();
            Axios
                .get("127.0.0.1:8000/movie_detail/", {
                    params:{
                        imdbid: this.imdbid,
                        username: this.username
                    }
                })
                .then(response => (this.movieDetailes = response))
                .catch(function(error){
                    console.log(error);
                });
        },
        methods: {
            onSubmitComment() {
                console.log('submit!');
            },
            getImdbID:function(){
                var routerImdbID = this.$route.query.imdbid
                var routerUserName = this.$router.query.username
                console.log(routerImdbID, routerUserName)
                this.imdbid = routerImdbID
                this.username = routerUserName
            },
            UploadComment(){
                Axios
                    .post("127.0.0.1:8000/movie_detail/", {
                        params:{
                            imdbid: this.imdbid,
                            username: this.username,
                        }
                    })
                    .then(response => (this.movieDetailes = response))
                    .catch(function(error){
                        console.log(error);
                    });
            }
        }
    }
</script>