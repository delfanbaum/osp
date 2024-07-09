extern crate rocket;
use rocket::{get, launch, routes};
use rocket::fs::FileServer;
use rocket_dyn_templates::{context, Template};
mod story;
use story::{get_node_by_id, StoryNode};

#[get("/")]
fn index() -> Template {
    let beginning: StoryNode = get_node_by_id(1).expect(
        // this expect is bad, fix!
        "Unable to find beginning",
    );
    Template::render(
        "index",
        context! {
        storynode: beginning},
    )
}

#[get("/<id>")]
fn story_route(id: u8) -> Template {
    let node: StoryNode = get_node_by_id(id).expect(
        // this expect is bad, fix!
        "Unable to find the requisite node!",
    );
    Template::render(
        "story",
        context! {
        storynode: node},
    )
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .mount("/", routes![index])
        .mount("/static/", FileServer::from("static"))
        .mount("/story/", routes![story_route])
        .attach(Template::fairing())
}
