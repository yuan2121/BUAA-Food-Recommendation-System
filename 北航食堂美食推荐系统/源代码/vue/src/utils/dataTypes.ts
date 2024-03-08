export interface SummaryData {
    id: number,
    comment_id?: number,
    cover: string,
    sign: string,
    imgHeight?: number,
    heart_clicked?: boolean,
    sub_title1: string,
    sub_title2: string,
    tags: string[]
}

export interface CommentData {
    id: number,
    commentname: string,
    rate: number,
    time: string,
    support: number,
    content: string,
    subcomments: []
}

export interface SubCommentData {
    id: number,
    commentedid: string,
    commenterid: string,
    time: string,
    support: number,
    content: string
}

export interface RankItem {
    name: string,
    link: string
}

export interface PreferenceTag {
    name: string,
    attitude: boolean
}

// interface for /search/search
export interface ResultSearch {
    code: number,
    dishes: DishSummary[]
}

export interface DishSummary {
    id: number,
    name: string,
    hall: string,
    tags: string[],
    purchase: number,
    comment: number,
    collectNum: number,
    score: number,
    window: string,
    'type': string
}

// interface for /search/search
export interface ParamSearch {
    keyword: string,
    hall: string[],
    order: OrderMethod,
    filters: TagsOnSearch,
    'type': string,
}

export type OrderMethod = 'score' | 'collect' | 'sales'

class TagsOnSearch {
    [name: string]: boolean
}
export const preferenceTagOnSearch = (tags: PreferenceTag[]) => {
    let dict = new TagsOnSearch()
    for (let tag of tags) {
        dict[tag.name] = tag.attitude
    }
    return dict
}

export interface ParamPostComment {
    user_id: string,
    dish_id: number,
    content: string,
    score: number,
    time: string
}

export interface CommentSummary {
    id: number,
    dish_id: number,    // 表示这是对哪一个菜品的评论
    user_id: string,    // 表示发布者id
    summary: string,    // 内容摘要，即最多 50 字的前缀
    score: number,      // 评分
    likes: number,      // 点赞数
    comments: number,   // 评论数
}

export interface HallAndWindow {
    hall: string,
    window: string,
}