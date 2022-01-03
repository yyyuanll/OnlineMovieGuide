const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: "/login",
    name: "login",
    component: () => import("pages/Login.vue")
  },
  {
    path:"/register",
    name:"register",
    component: () => import("pages/register.vue")

  },
  {
    path: '/page1',
    component: () => import('layouts/MainLayout1.vue'),
    children: [
      { path: '/page1', component: () => import('pages/Page1.vue') },
      { path: '/page2', component: () => import('pages/Page2.vue') },
      { path: '/page3', component: () => import('pages/Page3.vue') },
      { path: '/page4', component: () => import('pages/Page4.vue')},
      { path: '/page5', component: () => import('pages/Page5.vue') },
      { path: '/page6',
        component: () => import('pages/Page6.vue'), 
        redirect:'/page6/chart',
        children:[{
            path:'history',
            component: () => import('pages/history.vue')},
            {
                path:'favorite',
                component: () => import('pages/favorite.vue')},
                {
                    path:'chart',
                    component: () => import('pages/chart.vue')}
            ]
    }

    ]
  },
  {
    path: "/403",
    name: "403",
    component: () => import("pages/Error403")
  },
  {
    path: '/MovieDetails',
    component: () => import('layouts/MainLayout1.vue'),
    children: [
      { path: '/MovieDetails', name: 'MovieDetails', component: () => import('pages/MovieDetails.vue') }
    ]
  },
  

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
