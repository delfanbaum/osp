use std::fs;
use anyhow::Result;

use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct Fork {
    id: u8,
    text: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct StoryNode {
    id: u8,
    text: String,
    forks: Vec<Fork>,
}

fn read_in_story() -> Result<Vec<StoryNode>> {
    let story_json = fs::read_to_string("./un-conte.json").expect("Unable to read the story!");

    let story: Vec<StoryNode> =
        serde_json::from_str(&story_json)?;
    Ok(story)
}

pub fn get_node_by_id(id: u8) -> Result<StoryNode> {
    let story = read_in_story()?;
    match story.into_iter().find(|n| n.id == id) {
        Some(n) => Ok(n),
        None => Err(anyhow::anyhow!("Error, no StoryNode with id {} found", id))?
    }
}
