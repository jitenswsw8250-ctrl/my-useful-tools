package com.example.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

/**
 * Clean, Google AdSense policy-compliant placeholder.
 * Features:
 * - Clear, mandatory "ADVERTISEMENT" identification label
 * - Unmistakable border separation to prevent accidental user clicks
 * - Standard responsive ad aspect ratio / sizes
 * - Zero misleading elements or auto-click triggers
 */
@Composable
fun AdSensePlaceholder(
  modifier: Modifier = Modifier,
  slotLabel: String = "Responsive Display Ad (320x50 / 728x90)",
  height: Dp = 80.dp
) {
  Column(
    modifier = modifier
      .fillMaxWidth()
      .padding(vertical = 12.dp),
    horizontalAlignment = Alignment.CenterHorizontally
  ) {
    // Policy required label
    Text(
      text = "ADVERTISEMENT",
      style = MaterialTheme.typography.labelSmall,
      color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.7f),
      letterSpacing = 1.2.sp,
      fontWeight = FontWeight.SemiBold,
      fontSize = 10.sp,
      modifier = Modifier.padding(bottom = 4.dp)
    )

    Box(
      modifier = Modifier
        .fillMaxWidth()
        .height(height)
        .clip(RoundedCornerShape(8.dp))
        .background(MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.5f))
        .border(
          width = 1.dp,
          color = MaterialTheme.colorScheme.outline.copy(alpha = 0.4f),
          shape = RoundedCornerShape(8.dp)
        )
        .testTag("adsense_placeholder"),
      contentAlignment = Alignment.Center
    ) {
      Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp)
      ) {
        Text(
          text = "Google AdSense Placement Area",
          style = MaterialTheme.typography.bodyMedium,
          fontWeight = FontWeight.Medium,
          color = MaterialTheme.colorScheme.onSurfaceVariant,
          textAlign = TextAlign.Center
        )
        Spacer(modifier = Modifier.height(2.dp))
        Text(
          text = slotLabel,
          style = MaterialTheme.typography.bodySmall,
          fontFamily = FontFamily.Monospace,
          fontSize = 11.sp,
          color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.75f),
          textAlign = TextAlign.Center
        )
      }
    }
  }
}
