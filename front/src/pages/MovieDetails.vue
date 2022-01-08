<template>
    <div class="Stage">
        <div class="Details">
            <div class="left">
                <div class="title">
                {{movieDetailes[0].title}}<i :class='userLike' style="color: yellow" @click="UploadUserLike()"></i>
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
                        v-model="userRating"
                        :colors="colors"
                        @change="UploadRating()">
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
                    <el-card><img v-bind:src="movieDetailes[6].img" v-bind:alt="movieDetailes[6].title" style="height:230px;width:160px"><router-link :to="{name:'MovieDetails',query:{imdbid: movieDetailes[6].imdbid, username: this.username}}" class="link">{{movieDetailes[6].title}}</router-link></el-card>
                    <el-card><img v-bind:src="movieDetailes[7].img" v-bind:alt="movieDetailes[7].title" style="height:230px;width:160px"><router-link :to="{name:'MovieDetails',query:{imdbid: movieDetailes[7].imdbid, username: this.username}}" class="link">{{movieDetailes[7].title}}</router-link></el-card>
                    <el-card><img v-bind:src="movieDetailes[8].img" v-bind:alt="movieDetailes[8].title" style="height:230px;width:160px"><router-link :to="{name:'MovieDetails',query:{imdbid: movieDetailes[8].imdbid, username: this.username}}" class="link">{{movieDetailes[8].title}}</router-link></el-card>
                    <el-card><img v-bind:src="movieDetailes[9].img" v-bind:alt="movieDetailes[9].title" style="height:230px;width:160px"><router-link :to="{name:'MovieDetails',query:{imdbid: movieDetailes[9].imdbid, username: this.username}}" class="link">{{movieDetailes[9].title}}</router-link></el-card>
                    <el-card><img v-bind:src="movieDetailes[10].img" v-bind:alt="movieDetailes[10].title" style="height:230px;width:160px"><router-link :to="{name:'MovieDetails',query:{imdbid: movieDetailes[10].imdbid, username: this.username}}" class="link">{{movieDetailes[10].title}}</router-link></el-card>
                </div>
            </div>
            <div class="right">
                <div class="comment">
                    <el-card><p>{{movieDetailes[5].review1}}</p></el-card>
                    <el-card><p>{{movieDetailes[5].review2}}</p></el-card>
                    <el-card><p>{{movieDetailes[5].review3}}</p></el-card>
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
    </div>
</template>

<style>
    .left{
        float: left;
    }
    .right{
        float: right;
        height: 800px;
        overflow-y: scroll;
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
    .recommend{
        width: 100%;
        background-color: #f2f2f2;
        height: 280px;
        float: left;
    }
    .comment .el-card__body{
        height: auto;
    }
    .comment .el-card{
        height: auto;
    }
    .recommend .el-card{
        width: 20% !important;
        height: 100%;
        float: left;
    }
    .recommend .el-card__body{
        width: 100% !important;
        height: 100%;
    }
    .recommend img{
        /* width: 100%;
        height: auto; */
    }
    .link{
        text-decoration: none;
        color: #000;
    }
    a{
        text-decoration: none;
        font-style: italic;
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
                userRating: null,
                colors: ['#99A9BF', '#F7BA2A', '#FF9900'],  // 等同于 { 2: '#99A9BF', 4: { value: '#F7BA2A', excluded: true }, 5: '#FF9900' }
                userLike: 'el-icon-star-off',
                form: {
                        comment: '',
                    },
                movieDetailes:[
                    // [
                    //     {"title": "The Cut", "image": "http://127.0.0.1:8000/images/none.jpg", "imdbrating": 0.0, "imdbid": "tt5028408", "metascore": 0, "day": 19, "month": 9, "year": 2015, "runtime": "6 min", "rated": "N/A", "award": "N/A", "director": "Jeroen Pool", "writer": "N/A"}, 
                    //     {"genre1": "Documentary", "genre2": "Short"}, 
                    //     {"language1": "English"}, 
                    //     {"country1": "Netherlands", "country2": "UK", "country3": "N/A"}, 
                    //     {"actor1": "N/A", "actor_link1": "https://en.wikipedia.org/wiki/N/A"}, 
                    //     {"user1": "Nichole Crosby", "profile1": "https://a.academia-assets.com/assets/s200_no_pic-a1085ffe81e600887dffbe298fb865081a5861c588a68004201d7eddcfa95db3.png", "review1": "Last week was my third visit to NOCA.Since it was a Thursday, I had the wagyu pastrami sliders.  They were very good.  Thick pieces of meat on nicely toasted bread.  House made chips were great on the side.Good service.  Top-quality restaurant all around.", "star1": 8.0, "user2": "Emmanuel Colon", "profile2": "https://a.academia-assets.com/assets/s200_no_pic-a1085ffe81e600887dffbe298fb865081a5861c588a68004201d7eddcfa95db3.png", "review2": "Threw a friend's baby shower here and it went pretty smoothly. We made reservations well in advance, and it was a small party. I'm not a huge fan of their food but it's always busy so clearly other people don't have my same opinion. The three stars is for the service, they were super attentive and everything was taken care of for our party. I just don't think the cheesecake is that great, I'm sorry! But the apps aren't too bad.", "star2": 6.0, "user3": "Lucas Kim", "profile3": "https://a.academia-assets.com/assets/s200_no_pic-a1085ffe81e600887dffbe298fb865081a5861c588a68004201d7eddcfa95db3.png", "review3": null, "star3": 6.0}, 
                    //     {"imdbid": "tt1129381", "title": "Lower Learning", "img": "http://127.0.0.1:8000/images/tt1129381.jpg"}, 
                    //     {"imdbid": "tt1291150", "title": "Teenage Mutant Ninja Turtles", "img": "http://127.0.0.1:8000/images/tt1291150.jpg"}, 
                    //     {"imdbid": "tt1570989", "title": "Tiny Furniture", "img": "http://127.0.0.1:8000/images/tt1570989.jpg"}, 
                    //     {"imdbid": "tt2967224", "title": "Hot Pursuit", "img": "http://127.0.0.1:8000/images/tt2967224.jpg"}, 
                    //     {"imdbid": "tt4819544", "title": "Only You", "img": "http://127.0.0.1:8000/images/tt4819544.jpg"}
                    // ]
                ]
                
            }
        },
        created(){
            this.Refresh()
        },
        watch:{
            '$route': 'Refresh'
        },
        methods: {
            Refresh:function(){
                this.getImdbID();
                this.userRating = null;
                this.userLike = 'el-icon-star-off'
                Axios
                    .get("http://127.0.0.1:8000/movie_detail/", {
                        params:{
                            imdbid: this.imdbid,
                            username: this.username
                        }
                    })
                    .then(response => (this.movieDetailes = response.data))
                    .catch(function(error){
                        console.log(error);
                    });
            },
            onSubmitComment() {
                this.UploadComment()
            },
            getImdbID:function(){
                var routerImdbID = this.$route.query.imdbid
                var routerUserName = this.$route.query.username
                console.log(routerImdbID, routerUserName)
                this.imdbid = routerImdbID
                this.username = routerUserName
            },
            UploadComment(){
                let data = new FormData();
                data.append('imdbid', this.imdbid);
                data.append('username', this.username);
                data.append('review', this.form.comment);
                Axios
                    .post("http://127.0.0.1:8000/user/add_comment/", data)
                    .catch(function(error){
                        console.log(error);
                    });
            },
            UploadRating(){
                let data = new FormData();
                data.append('imdbid', this.imdbid);
                data.append('username', this.username);
                data.append('star', this.userRating);
                Axios
                    .post("http://127.0.0.1:8000/user/add_star/", data)
                    .catch(function(error){
                        console.log(error);
                    });
            },
            UploadUserLike(){
                if(this.userLike == 'el-icon-star-on'){
                    let data = new FormData();
                    data.append('imdbid', this.imdbid);
                    data.append('username', this.username);
                    Axios
                        .post("http://127.0.0.1:8000/user/remove_fav/")
                        .then(response=>{
                            if(response.data[0].status == 200){
                                this.userLike = 'el-icon-star-off'
                            }
                        })
                        .catch(function(error){
                            console.log(error);
                        });
                }
                else{
                    let data = new FormData();
                    data.append('imdbid', this.imdbid);
                    data.append('username', this.username);
                    Axios
                        .post("http://127.0.0.1:8000/user/add_fav/")
                        .then(response=>{
                            if(response.data[0].status == 200){
                                this.userLike = 'el-icon-star-on'
                            }
                        })
                        .catch(function(error){
                            console.log(error);
                        });
                }
            }
        }
    }
</script>