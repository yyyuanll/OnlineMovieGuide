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
      { path: '/page1', component: () => import('pages/Page1.vue') }
    ]
  },
  {
    path: '/page4',
    component: () => import('layouts/MainLayout1.vue'),
    children: [
      { path: '/page4', component: () => import('pages/Page4.vue') }
    ]
  },
  {
    path: '/page5',
    component: () => import('layouts/MainLayout1.vue'),
    children: [
      { path: '/page5', component: () => import('pages/Page5.vue') }
    ]
  },
  {
    path: "/403",
    name: "403",
    component: () => import("pages/Error403")
  },
  

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
