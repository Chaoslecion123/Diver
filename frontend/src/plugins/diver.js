import Vue from 'vue'

import '@/assets/styles/main.less'
import '@/components/_styles'
import '@/views/Account/style'
import '@/views/Auth/style'
import '@/views/Error/style.less'

// import Address from '@/components/d-address'
import Brand from '@/components/d-brand'

import AddComment from '@/components/d-add-comment'
import AddToFavorite from '@/components/d-add-favorite-popup'
import Categories from '@/components/d-categories'
import CategoryFilter from '@/components/d-category-filter'
import CategoryMenu from '@/components/d-category-menu'
import CommentBox from '@/components/d-comment-box'
import EditEmail from '@/components/d-edit-email-popup'
import EditPassword from '@/components/d-edit-password-popup'
import Footer from '@/components/d-footer'
import HeaderCarousel from '@/components/d-header-carousel'
import HomeCarousel from '@/components/d-home-carousel'
import Login from '@/components/d-login-popup'
import NavigationDrawer from '@/components/d-navigation-drawer'
import NewAddress from '@/components/d-new-address-popup'
import NewBill from '@/components/d-new-bill-popup'
import OrderDetailsCard from '@/components/d-checkout-sumary'
import Pagination from '@/components/d-pagination'
import Popup from '@/components/d-popup'

import Product from '@/components/d-product'

import Rating from '@/components/d-rating'
import SearchField from '@/components/d-search-field'
import ShareUs from '@/components/d-share-popup'
import Showcase from '@/components/d-showcase'
import StoreMenu from '@/components/d-store-menu'
import SystemBar from '@/components/d-system-bar'
import Toolbar from '@/components/d-toolbar'

// Vue.component('d-address-form', Address.Form)
// Vue.component('d-address-popup', Address.Popup)

Vue.component('d-brand-carousel', Brand.Carousel)
Vue.component('d-brand-featured-carousel', Brand.Featured.Carousel)

Vue.component('d-add-comment', AddComment)
Vue.component('d-add-favorite-popup', AddToFavorite)
Vue.component('d-categories', Categories)
Vue.component('d-category-filter', CategoryFilter)
Vue.component('d-category-menu', CategoryMenu)
Vue.component('d-comment-box', CommentBox)
Vue.component('d-edit-email-popup', EditEmail)
Vue.component('d-edit-password-popup', EditPassword)
Vue.component('d-footer', Footer)
Vue.component('d-header-carousel', HeaderCarousel)
Vue.component('d-home-carousel', HomeCarousel)
Vue.component('d-login-popup', Login)
Vue.component('d-navigation-drawer', NavigationDrawer)
Vue.component('d-new-address-popup', NewAddress)
Vue.component('d-new-bill-popup', NewBill)
Vue.component('d-checkout-sumary', OrderDetailsCard)
Vue.component('d-pagination', Pagination)
Vue.component('d-popup', Popup)
Vue.component('d-product-card', Product.Card)
Vue.component('d-product-showcase', Product.Showcase)
Vue.component('d-product-quantity', Product.Quantity)
Vue.component('d-product-attributes', Product.Attributes)
Vue.component('d-product-filter', Product.Filter)
Vue.component('d-rating', Rating)
Vue.component('d-search-field', SearchField)
Vue.component('d-share-popup', ShareUs)
Vue.component('d-showcase', Showcase)
Vue.component('d-store-menu', StoreMenu)
Vue.component('d-system-bar', SystemBar)
Vue.component('d-toolbar', Toolbar)
