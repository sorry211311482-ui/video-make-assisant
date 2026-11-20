// SPDX-License-Identifier: MIT
// Adapted from vibe-knowledge stamp(), Copyright (c) 2026 Berryxia (andyhuo520).
// https://github.com/andyhuo520/vibe-knowledge/blob/c3a13a85f7cc560e5d396f063baecea4b2748e1e/skills/vibe-knowledge/kit/know.js#L410-L419

window.addVideoProductionStamp = function addVideoProductionStamp(timeline, node, at) {
  timeline.fromTo(node, { opacity: 0 }, { opacity: 1, duration: 0.06, ease: "none" }, at);
  timeline.fromTo(node, { scale: 1.6 }, { scale: 1, duration: 0.18, ease: "power2.out" }, at);
};
